import aocd, sys

inp = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=15, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

import re

def HASH(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

steps = inp.split(",")
boxes = [dict() for _ in range(256)]

part1 = 0
for step in steps:
    part1 += HASH(step)
    box, ins = re.split(r"[-=]", step)
    if len(ins) > 0:
        boxes[HASH(box)][box] = int(ins)
    elif box in boxes[HASH(box)]:
        del boxes[HASH(box)][box]

part2 = sum((box_nr + 1) * (i + 1) * focal_length for box_nr in range(256) for i, focal_length in enumerate(boxes[box_nr].values()))

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=15, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=15, year=2023)
