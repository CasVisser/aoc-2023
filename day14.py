import aocd, sys

inp = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=14, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

lines = list(map(list, inp.split("\n")))
seen = {tuple(map(tuple, lines)): 1000000000}

def tilt(grid):
    for row in range(1, len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "O":
                new_row = row - 1
                while new_row >= 0 and grid[new_row][col] == ".":
                    grid[new_row + 1][col] = "."
                    grid[new_row][col] = "O"
                    new_row -= 1

tilt(lines)
part1 = sum([row.count("O") * (len(lines) - i) for i, row in enumerate(lines)])

cycles_left = 1000000000
while cycles_left > 0:
    for _ in range(4):
        tilt(lines)
        lines = list(map(list, zip(*reversed(lines))))
    tup = tuple(map(tuple, lines))
    cycles_left -= 1
    if tup in seen:
        cycles_left = cycles_left % (seen[tup] - cycles_left)
    seen[tup] = cycles_left

part2 = sum([row.count("O") * (len(lines) - i) for i, row in enumerate(lines)])

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=14, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=14, year=2023)
