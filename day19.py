import aocd, sys

inp = r"""px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=19, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

from collections import defaultdict
from copy import deepcopy
from math import prod

workflows_inp, parts_inp = map(str.split, inp.split("\n\n"))

parts = [{c: int(v[2:]) for c, v in zip("xmas", part[1:-1].split(","))} for part in parts_inp]
workflows = defaultdict(list)
for l in workflows_inp:                               # runnings example: "px{a<2006:qkq,m>2090:A,rfg}"
    name, instructions = l.split("{")                 # ["px", "a<2006:qkq,m>2090:A,rfg}"]
    workflows[name] = instructions[:-1].split(",")    # ["a<2006:qkq", "m>2090:A", "rfg"]

# yields (ranges, destination)
def apply_rules_ranges(rules, ranges):            # ranges :: c:[start, end] incl.
    for rule in rules[:-1]:                       # "a<2006:qkq"
        condition, destination = rule.split(":")  # ["a<2006", "qkq"]
        category, comp = condition[:2]            # "a", "<"
        boundary = int(condition[2:])             # 2006
        ranges_in_boundary = deepcopy(ranges)
        if comp == "<":
            ranges_in_boundary[category][1] = boundary - 1
            ranges[category][0] = boundary
        elif comp == ">":
            ranges_in_boundary[category][0] = boundary + 1
            ranges[category][1] = boundary
        yield (ranges_in_boundary, destination)
    yield (ranges, rules[-1])

todo = [({c: [1, 4000] for c in "xmas"}, "in")]
accepted_ranges = []
while len(todo) > 0:
    ranges, destination = todo.pop(0)
    if destination == "A": 
        accepted_ranges.append(ranges)
        continue
    if destination not in workflows: continue
    for t in apply_rules_ranges(workflows[destination], ranges):
        todo.append(t)

part1 = sum(sum(p.values()) for p in parts if any(all(r[c][0] <= p[c] <= r[c][1] for c in "xmas") for r in accepted_ranges))
part2 = sum(prod(r[1] - r[0] + 1 for r in ranges.values()) for ranges in accepted_ranges)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=19, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=19, year=2023)
