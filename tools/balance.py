"""Balance check for Zenthium SWIFT Heroes.

Reads the CSV files in design/data/, applies the formulas from design/balance.md,
and reports the real numbers with budget flags.

Usage:
  python3 tools/balance.py report        Print anchors, modules and prices.
  python3 tools/balance.py xlsx [path]   Write a spreadsheet view (default build/balance_view.xlsx).
                                         The view is for exploring only; numbers live in the CSVs.
"""
import csv
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "design", "data")

# A module is flagged when its damage is this far off its budget.
FLAG_HIGH = 1.5
FLAG_LOW = 0.5


def read_csv(name):
    with open(os.path.join(DATA, name), newline="") as f:
        return list(csv.DictReader(f))


def load_constants():
    c = {}
    for row in read_csv("constants.csv"):
        v = row["value"]
        try:
            v = float(v)
        except ValueError:
            pass
        c[row["name"]] = v
    return c


C = load_constants()


def tier(scale, name):
    return C.get(f"{scale}.{name}") if name else None


def normal_damage(stat):
    return C["normal_damage_base"] + C["normal_damage_per_stat"] * stat


def hp(toughness, leader=False):
    return C["hp_per_toughness"] * toughness * (C["leader_hp_multiplier"] if leader else 1)


def armor(toughness):
    return C["armor_per_toughness"] * toughness


def hit(damage, target_toughness):
    return max(damage - armor(target_toughness), damage * C["min_damage_fraction"])


def rank_stats(innate, rank_index=0):
    """Stats of a rank-tier entity: base 10, innate boost plus the difficulty bonus, added."""
    return C["goon_stat"] * (1 + innate + C["stat_bonus_per_rank"] * rank_index)


def module_cooldown(row):
    if row["cooldown_s"]:
        return float(row["cooldown_s"])
    if row["cost"]:
        return float(row["cost"]) * C["resource_seconds_per_point"]
    return None


def module_budget(row):
    """Returns (damage multiplier, cooldown, budget multiplier, ratio, flag)."""
    mult = tier("damage", row["damage_tier"])
    cd = module_cooldown(row)
    if mult is None or cd is None:
        return mult, cd, None, None, ""
    budget = cd / C["kick_cooldown"] * (tier("utility", row.get("utility") or "None") or 1)
    ratio = mult / budget
    flag = "OVER" if ratio > FLAG_HIGH else "UNDER" if ratio < FLAG_LOW else ""
    if flag and row.get("budget_ok") == "Checked":
        flag = "ok (checked)"
    return mult, cd, budget, ratio, flag


def anchors():
    lo, hi = C["hero_stat_low"], C["hero_stat_high"]
    rows = []
    for label, innate, leader in (("goon", C["innate_boost_goon"], False),
                                  ("Champion", C["innate_boost_champion"], False),
                                  ("Leader", C["innate_boost_leader"], True)):
        s = rank_stats(innate)
        h = hp(s, leader)
        kicks = [math.ceil(h / hit(normal_damage(st), s)) for st in (hi, lo)]
        rows.append((f"Kicks to defeat a rank D {label}", f"{kicks[0]}-{kicks[1]}"))
    goon_hit = normal_damage(C["goon_stat"]) * tier("damage", C["enemy_default_damage_tier"])
    survived = [math.ceil(hp(t) / hit(goon_hit, t)) for t in (lo, hi)]
    rows.append(("Goon hits a starting hero survives", f"{survived[0]}-{survived[1]}"))
    return rows


def parse_values(text):
    out = {}
    for part in (text or "").split(";"):
        if "=" in part:
            k, v = part.split("=", 1)
            v = v.strip()
            try:
                v = float(v)
            except ValueError:
                pass
            out[k.strip()] = v
    return out


def starting_kits():
    """First module of each type for every preset, read from the Kits table in design/heroes.md."""
    kits = {}
    path = os.path.join(ROOT, "design", "heroes.md")
    in_kits = False
    for line in open(path):
        if line.startswith("### Kits"):
            in_kits = True
            continue
        if in_kits and line.startswith("## "):
            break
        if in_kits and line.startswith("| ") and not line.startswith("| Hero") and not line.startswith("|---"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            first = [c.split(",")[0].split("(")[0].strip() for c in cells[1:4]]
            kits[cells[0]] = first
    return kits


def benchmark(goons=4):
    mods = {m["module"]: m for m in read_csv("modules.csv")}
    kits = starting_kits()
    goon = C["goon_stat"]
    goon_hp = hp(goon)
    goon_hit = normal_damage(goon) * tier("damage", C["enemy_default_damage_tier"])
    goon_interval = 1.5
    results = []
    for h in read_csv("heroes.csv"):
        if h["starter"] != "yes":
            continue
        stat = {k: float(h[k]) for k in ("strength", "will", "intelligence", "finesse", "toughness")}
        active, passive, gear = kits[h["hero"]]
        notes = []
        # The hero's best attack among Kick and their starting active and gear.
        best = (0, "Kick")
        for name in ("Kick", active, gear):
            m = mods.get(name)
            if not m or not m["damage_tier"]:
                continue
            per_hit = hit(normal_damage(stat[m["stat"].lower()]) * tier("damage", m["damage_tier"]), goon)
            if m["cooldown_s"]:
                interval = float(m["cooldown_s"])
            else:
                interval = 1.0
                pool = float(m["cost"]) + parse_values(mods[passive]["values"]).get(m["resource"].lower(), 0)
                notes.append(f"{name}: {int(pool // float(m['cost']))} shots per full {m['resource']}")
            dps = per_hit / interval
            if dps > best[0]:
                best = (dps, name)
        dps, attack = best
        # Summons fight alongside the hero, and Spell Tomes add to their hits.
        summon = parse_values(mods[active]["values"]).get("summon_attack") if active in mods else None
        if summon:
            sm = mods[summon]
            bonus = parse_values(mods[gear]["values"]).get("magic_hit_damage", 0) if gear in mods else 0
            s_hit = hit(normal_damage(stat[sm["stat"].lower()]) * tier("damage", sm["damage_tier"]) + bonus, goon)
            dps += s_hit / float(sm["cooldown_s"])
            attack += f" + {active}"
        per_goon = goon_hp / dps
        total = per_goon * goons
        dodge = min(stat["finesse"] * C["dodge_per_finesse"], C["dodge_cap"])
        taken_per_s = hit(goon_hit, stat["toughness"]) / goon_interval * (1 - dodge)
        goon_seconds = per_goon * sum(range(1, goons + 1))
        taken = taken_per_s * goon_seconds
        max_hp = hp(stat["toughness"])
        saved = parse_values(mods[passive]["values"]).get("defiance_chance_bonus", 0) >= 1 if passive in mods else False
        if taken < max_hp:
            outcome = "survives"
        elif saved:
            outcome = "survives thanks to a guaranteed Defiance"
        else:
            outcome = "goes down"
        results.append((h["hero"], attack, total, taken, max_hp, outcome, notes))
    return results


def prices():
    income = {"basic": C["income_basic"], "gem": C["income_gem"], "metallic": C["income_metallic"]}
    out = []
    for p in read_csv("prices.csv"):
        cur = p["currency"]
        out.append((p["purchase"], p["missions"], cur, float(p["missions"]) * income[cur]))
    return out


def fmt(x):
    if x is None or x == "":
        return "-"
    if isinstance(x, float):
        return f"{x:g}" if x == int(x) else f"{x:.2f}"
    return str(x)


def report():
    print("== Anchors (compare with design/balance.md section 3) ==")
    for name, value in anchors():
        print(f"  {name}: {value}")

    mods = read_csv("modules.csv")
    filled = [m for m in mods if m["damage_tier"] or m["cooldown_s"] or m["cost"] or m.get("values")]
    print(f"\n== Modules ({len(filled)} of {len(mods)} have numbers) ==")
    print(f"  {'Module':24} {'Tier':8} {'Utility':8} {'Cooldown':>8} {'Dmg@10':>7} {'Dmg@20':>7} {'Budget':>7} {'Ratio':>6}  Flag")
    for m in filled:
        mult, cd, budget, ratio, flag = module_budget(m)
        d10 = normal_damage(10) * mult if mult is not None else None
        d20 = normal_damage(20) * mult if mult is not None else None
        print(f"  {m['module']:24} {m['damage_tier'] or '-':8} {m.get('utility') or 'None':8} {fmt(cd):>8} {fmt(d10):>7} {fmt(d20):>7} {fmt(budget):>7} {fmt(ratio):>6}  {flag}")

    print("\n== Benchmark: starting heroes, starting slots only, against 4 rank D goons at once ==")
    print("  (No positioning, kiting or healing; real fights are gentler.)")
    for name, attack, total, taken, max_hp, outcome, notes in benchmark():
        print(f"  {name:16} {attack:30} clears in {total:5.1f} s, takes {taken:5.0f} of {max_hp:g} HP: {outcome}")
        for n in notes:
            print(f"  {'':16} {n}")

    print("\n== Prices ==")
    for purchase, missions, cur, price in prices():
        print(f"  {purchase:22} {missions:>4} missions -> {fmt(price)} {cur}")


def xlsx(path):
    from openpyxl import Workbook
    from openpyxl.formatting.rule import FormulaRule
    from openpyxl.styles import Font, PatternFill
    from openpyxl.worksheet.datavalidation import DataValidation

    wb = Workbook()
    bold = Font(bold=True)

    cs = wb.active
    cs.title = "Constants"
    cs.append(["name", "value", "notes"])
    for row in read_csv("constants.csv"):
        v = row["value"]
        try:
            v = float(v)
        except ValueError:
            pass
        cs.append([row["name"], v, row["notes"]])
    for cell in cs[1]:
        cell.font = bold

    def const(name):
        return f'VLOOKUP("{name}",Constants!$A:$B,2,FALSE)'

    ms = wb.create_sheet("Modules")
    head = ["module", "category", "stat", "damage_tier", "cooldown_s", "resource", "cost", "utility",
            "cooldown used", "damage x", "damage @10", "damage @20", "budget x", "ratio", "budget_ok"]
    ms.append(head)
    for cell in ms[1]:
        cell.font = bold
    mods = read_csv("modules.csv")
    for i, m in enumerate(mods, start=2):
        ms.append([m["module"], m["category"], m["stat"], m["damage_tier"],
                   float(m["cooldown_s"]) if m["cooldown_s"] else None, m["resource"],
                   float(m["cost"]) if m["cost"] else None, m.get("utility") or "None"])
        ms[f"I{i}"] = f'=IF(E{i}<>"",E{i},IF(G{i}<>"",G{i}*{const("resource_seconds_per_point")},""))'
        ms[f"J{i}"] = f'=IF(D{i}="","",VLOOKUP("damage."&D{i},Constants!$A:$B,2,FALSE))'
        ms[f"K{i}"] = f'=IF(J{i}="","",({const("normal_damage_base")}+{const("normal_damage_per_stat")}*10)*J{i})'
        ms[f"L{i}"] = f'=IF(J{i}="","",({const("normal_damage_base")}+{const("normal_damage_per_stat")}*20)*J{i})'
        ms[f"M{i}"] = f'=IF(I{i}="","",I{i}/{const("kick_cooldown")}*VLOOKUP("utility."&H{i},Constants!$A:$B,2,FALSE))'
        ms[f"N{i}"] = f'=IF(OR(J{i}="",M{i}=""),"",J{i}/M{i})'
        ms[f"O{i}"] = m.get("budget_ok") or ""
    last = len(mods) + 1
    tiers = ",".join(n.split(".", 1)[1] for n in C if n.startswith("damage."))
    dv = DataValidation(type="list", formula1=f'"{tiers}"', allow_blank=True)
    ms.add_data_validation(dv)
    dv.add(f"D2:D{last}")
    uv = DataValidation(type="list", formula1='"None,Some,Strong"', allow_blank=True)
    ms.add_data_validation(uv)
    uv.add(f"H2:H{last}")
    red = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
    ms.conditional_formatting.add(
        f"A2:O{last}",
        FormulaRule(formula=[f'AND($N2<>"",$O2<>"Checked",OR($N2>{FLAG_HIGH},$N2<{FLAG_LOW}))'], fill=red))

    ps = wb.create_sheet("Prices")
    ps.append(["purchase", "missions", "currency", "price"])
    for cell in ps[1]:
        cell.font = bold
    for i, p in enumerate(read_csv("prices.csv"), start=2):
        ps.append([p["purchase"], float(p["missions"]), p["currency"]])
        ps[f"D{i}"] = f'=B{i}*VLOOKUP("income_"&C{i},Constants!$A:$B,2,FALSE)'

    an = wb.create_sheet("Anchors")
    an.append(["anchor", "value (calculated by the script)"])
    for cell in an[1]:
        cell.font = bold
    for row in anchors():
        an.append(list(row))

    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    wb.save(path)
    print(f"Wrote {path}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "report"
    if cmd == "report":
        report()
    elif cmd == "xlsx":
        xlsx(sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "build", "balance_view.xlsx"))
    else:
        print(__doc__)
