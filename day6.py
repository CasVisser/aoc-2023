import aocd, sys

inp = """Time:      7  15   30
Distance:  9  40  200"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=6, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

from math import ceil, floor, prod, sqrt

def n_wins(b, c): 
    x_min, x_max = (b - (d := sqrt(b**2 - 4 * c))) / 2, (b + d) / 2
    return floor(x_max - .001) - ceil(x_min + .001) + 1

times, dists = map(lambda line: [int(n) for n in line.split()[1:]], inp.split("\n"))

part1 = prod(n_wins(t, d) for t, d in zip(times, dists))
part2 = n_wins(int("".join(map(str, times))), int("".join(map(str, dists))))

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=6, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=6, year=2023)
