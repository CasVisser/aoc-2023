import aocd, sys

inp = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=11, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

from itertools import combinations

data = inp.split()
galaxies = []
row_size = [2] * len(data)
col_size = [2] * len(data[0])
row_size2 = [1000000] * len(data)
col_size2 = [1000000] * len(data[0])
for i, row in enumerate(data):
    for j, col in enumerate(row):
        if col == "#":
            galaxies.append((i, j))
            row_size[i] = col_size[j] = 1
            row_size2[i] = col_size2[j] = 1

part1 = part2 = 0
for (r1, c1), (r2, c2) in combinations(galaxies, 2):
    part1 += sum(row_size[min(r1, r2):max(r1, r2)]) + sum(col_size[min(c1, c2):max(c1, c2)]) 
    part2 += sum(row_size2[min(r1, r2):max(r1, r2)]) + sum(col_size2[min(c1, c2):max(c1, c2)]) 

### END SOLTUION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=11, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=11, year=2023)
