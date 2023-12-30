import aocd, sys

inp = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=3, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

from collections import defaultdict
from math import prod

lines = inp.split("\n")
chars = inp.replace("\n", "")
h = len(lines)
w = len(lines[0])

n_to_adj = defaultdict(set)
adj_to_n = defaultdict(set)
symbols = set()
potential_gears = set()

i = 0
while i < len(chars):
    if chars[i].isdigit(): # parse number
        j = min(j for j in range(i + 1, i + 4) if not chars[j].isdigit()) # there are no "wrap-around" numbers in the input, and numbers are at most 3 digits
        n = (int(chars[i:j]), i) # include i so duplicate numbers are handled separately
        area_coords = {(row, col) for row in range(i // w - 1, i // w + 2) for col in range(i % w - 1, i % w + j-i + 1)}
        adj_coords = area_coords - {(i // w, col) for col in range(i, j)} # this line could technically go without losing correctness, but I like it for efficiency and elegance
        n_to_adj[n] = adj_coords
        for coords in adj_coords: adj_to_n[coords].add(n)
        i = j
    if chars[i] == "*": potential_gears.add((i // w, i % w))
    if chars[i] != ".": symbols.add((i // w, i % w))
    i += 1

part1 = sum(n[0] for n, adj_coords in n_to_adj.items() if any(coords in symbols for coords in adj_coords))
part2 = sum(prod(map(lambda t: t[0], adj_to_n[gear])) for gear in potential_gears if len(adj_to_n[gear]) == 2)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=3, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=3, year=2023)
