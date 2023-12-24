import aocd, sys

inp = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

inp = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

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
loop_coords = {(s % (w + 1), s // (w + 1))}
queue = [(s % (w + 1), s // (w + 1))]

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

def next_turn(c):
    for x in range(c[0] + 1, w):
        if grid[x, c[1]] in "LFSJ7":
            return grid[x, c[1]]

part2 = 0
for y in range(h):
    inside_loop = False
    for x in range(w):
        if (x, y) in loop_coords:
            if (grid[x, y] == "|" 
                or (grid[x, y] == "L" and next_turn((x, y)) in "7S")
                or (grid[x, y] == "F" and next_turn((x, y)) in "JS")):
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
