import aocd, sys

inp = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

inp = """K295K 253
4T768 459
6J84Q 528
4929T 883
4QJ6K 458
QKJK3 571
264J3 527
4K547 808
K4JJJ 896
AK8K2 410
ATQ4J 371
55522 973
85583 738
99J22 674"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=7, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

from itertools import groupby
from functools import cmp_to_key

def hand_type1(hand):
    groups = sorted([list(g) for k, g in groupby(sorted(hand))], key=len, reverse=True)
    if len(groups[0]) == 5: return 7
    if len(groups[0]) == 4: return 6
    if len(groups[0]) == 3 and len(groups[1]) == 2: return 5
    if len(groups[0]) == 3: return 4
    if len(groups[0]) == 2 and len(groups[1]) == 2: return 3
    return len(groups[0])

def compare_lines1(x, y):
    val = {k: v for v, k in enumerate("23456789TJQKA")}
    h1, b1 = x.split()
    h2, b2 = y.split()
    if hand_type1(h1) != hand_type1(h2):
        return hand_type1(h1) - hand_type1(h2)
    for v1, v2 in zip(h1, h2):
        if val[v1] != val[v2]:
            return val[v1] - val[v2]
    return 0

def hand_type2(hand):
    n_jacks = hand.count("J")
    if n_jacks == 5: return 7
    groups = sorted([list(g) for k, g in groupby(sorted(hand.replace("J", "")))], key=len, reverse=True)
    if len(groups[0]) + n_jacks == 5: return 7
    if len(groups[0]) + n_jacks == 4: return 6
    if len(groups[0]) + n_jacks == 3 and len(groups[1]) == 2: return 5
    if len(groups[0]) + n_jacks == 3: return 4
    if len(groups[0]) + n_jacks == 2 and len(groups[1]) == 2: return 3
    return len(groups[0]) + n_jacks

def compare_lines2(x, y):
    val = {k: v for v, k in enumerate("J23456789TQKA")}
    h1, b1 = x.split()
    h2, b2 = y.split()
    if hand_type2(h1) != hand_type2(h2):
        return hand_type2(h1) - hand_type2(h2)
    for v1, v2 in zip(h1, h2):
        if val[v1] != val[v2]:
            return val[v1] - val[v2]
    return 0

lines = inp.split("\n")
lines.sort(key=cmp_to_key(compare_lines1))
part1 = 0
for rank, line in enumerate(lines):
    hand, bid = line.split()
    part1 += (rank + 1) * int(bid)

lines.sort(key=cmp_to_key(compare_lines2))
part2 = 0
for rank, line in enumerate(lines):
    hand, bid = line.split()
    part2 += (rank + 1) * int(bid)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=7, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=7, year=2023)
