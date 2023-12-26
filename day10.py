import aocd, sys

inp = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=10, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

connecting_dirs = { # (dx, dy)
    "S": [(0, -1), (1, 0), (0, 1), (-1, 0)],
    "|": [(0, -1),         (0, 1),        ],
    "-": [         (1, 0),         (-1, 0)],
    "L": [(0, -1), (1, 0),                ],
    "J": [(0, -1),                 (-1, 0)],
    "7": [                 (0, 1), (-1, 0)],
    "F": [         (1, 0), (0, 1),        ],
    ".": []
}
w = inp.index("\n")
h = len(inp) // w
s = inp.index("S")
grid = {(i % (w + 1), i // (w + 1)): x for i, x in enumerate(inp) if x != "\n"}
start = (s % (w + 1), s // (w + 1))
loop_coords = {start}
queue = [start]

def singly_connecting_neighbors(xy):
    return {(xy[0] + dx, xy[1] + dy) for dx, dy in connecting_dirs[grid[xy]] 
            if 0 <= xy[0] + dx < w and 0 <= xy[1] + dy < h}

def doubly_connecting_neighbors(xy):
    return {n for n in singly_connecting_neighbors(xy) if xy in singly_connecting_neighbors(n)}

while queue:
    cur = queue.pop(0)
    new = doubly_connecting_neighbors(cur) - loop_coords
    queue += new
    loop_coords |= new

part1 = len(loop_coords) // 2

step_over_chars = "|JL"
if (start[0], start[1] - 1) in doubly_connecting_neighbors(start): step_over_chars += "S"
part2 = 0
for y in range(h):
    inside_loop = False
    for x in range(w):
        if (x, y) in loop_coords:
            if grid[x, y] in step_over_chars:
                inside_loop = not inside_loop
        elif inside_loop:
            part2 += 1

### END SOLTUION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=10, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=10, year=2023)
