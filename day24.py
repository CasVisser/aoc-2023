import aocd, sys


inp = r"""19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=24, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

from z3 import Int, Solver

LOWER = 200000000000000
UPPER = 400000000000000

part2_requirements = []
s = Solver()
x = Int("x")
y = Int("y")
z = Int("z")
u = Int("u")
v = Int("v")
w = Int("w")

part1 = 0

hailstones = [tuple(map(int, line.replace(" @", ",").split(","))) for line in inp.split("\n")]
for i, hs1 in enumerate(hailstones):
    x1, y1, z1, u1, v1, w1 = hs1
    if i < 3: # part 2
        t = Int(f"t{i}")
        s.add(x + t * u == x1 + t * u1)
        s.add(y + t * v == y1 + t * v1)
        s.add(z + t * w == z1 + t * w1)
        s.add(t >= 0)
    for hs2 in hailstones[i + 1:]: # part 1
        x2, y2, z2, u2, v2, w2 = hs2
        if v1 == u1 * v2 / u2:
            continue # parallel
        t1 = (y2 - y1) / (v1 - u1 * v2 / u2) + (v2 * (x1 - x2)) / (v1 * u2 - u1 * v2)
        t2 = (x1 - x2 + t1 * u1) / u2
        if t1 < 0 or t2 < 0:
            continue # collision in past
        x_collision = x1 + t1 * u1
        if x_collision < LOWER or x_collision > UPPER:
            continue # outside AOI
        y_collision = y1 + t1 * v1
        if y_collision < LOWER or y_collision > UPPER:
            continue # outside AOI
        part1 += 1

s.check()
m = s.model()
print(f"{m[x]=} {m[y]=} {m[z]=} {m[u]=} {m[v]=} {m[w]=} ")
part2 = m[x].as_long() + m[y].as_long() + m[z].as_long()

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=24, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=24, year=2023)
