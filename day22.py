import aocd, sys

inp = r"""1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=22, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

from collections import defaultdict
from copy import deepcopy

def intersects(b1, b2): # two bricks intersect if they intersect in each dimension
    return (
        (b2[0][0] <= b1[0][0] <= b2[1][0] or b1[0][0] <= b2[0][0] <= b1[1][0]) and 
        (b2[0][1] <= b1[0][1] <= b2[1][1] or b1[0][1] <= b2[0][1] <= b1[1][1]) and 
        (b2[0][2] <= b1[0][2] <= b2[1][2] or b1[0][2] <= b2[0][2] <= b1[1][2]))

def b2t(b): # brick to tuple
    return (tuple(b[0]), tuple(b[1]))

bricks = [] # ([x, y, z], ...)

for l in inp.split():
    start, end = map(lambda x: list(map(int, x.split(","))), l.split("~"))
    bricks.append((start, end))
bricks.sort(key=lambda b: b[0][2]) # handle lowest bricks first

supporting = defaultdict(set)
supported_by = defaultdict(set)

for i, brick in enumerate(bricks):
    possible_intersecting_bricks = sorted(bricks[:i], key=lambda br: br[1][2], reverse=True) # sort for optimization
    while brick[0][2] > 1:
        brick[0][2] -= 1
        brick[1][2] -= 1
        intersecting_bricks = []
        for ib in possible_intersecting_bricks:
            if intersects(brick, ib):
                intersecting_bricks.append(ib)
            if ib[1][2] < brick[0][2]:
                break # highest ending bricks are considered first, so all further bricks are entirely below b
        if len(intersecting_bricks) > 0:
            brick[0][2] += 1
            brick[1][2] += 1
            for ib in intersecting_bricks:
                supporting[b2t(brick)].add(b2t(ib))
                supported_by[b2t(ib)].add(b2t(brick))
            break

part1 = len([b for b in bricks if all(len(supporting[b2t(sb)]) > 1 for sb in supported_by[b2t(b)])])

def remove_support(brick, supp):
    for supported_brick in supported_by[b2t(brick)]:
        supp[b2t(supported_brick)] -= {b2t(brick)}
        if len(supp[supported_brick]) == 0:
            remove_support(supported_brick, supp)

part2 = 0
for brick in bricks:
    supporting2 = deepcopy(supporting)
    remove_support(brick, supporting2)
    part2 += len([v for b, v in supporting2.items() if len(v) == 0 and b[0][2] > 1])

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=22, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=22, year=2023)
