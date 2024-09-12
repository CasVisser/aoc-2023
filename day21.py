import aocd, sys

inp = r""".................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##..S####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
................................."""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=21, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

width = inp.index("\n")
height = inp.count("\n") + 1
grid = {complex(i // width, i % width): c for i, c in enumerate(inp.replace("\n", ""))}
start = complex(height // 2, width // 2) # row, col

def neighbors(c):
    return {n for n in (c + 1, c - 1, c + 1j, c - 1j)
            if n in grid and grid[n] != "#"}

reachable_in = [{start}, neighbors(start)] # fix first two values for neat loop
q = neighbors(start)
for i in range(130): # i is two lower than len(reachable_in)
    new_reachable = set.union(*[neighbors(c) for c in q])
    q = new_reachable - reachable_in[i] # disregard going a step back
    reachable_in.append(new_reachable | reachable_in[i]) # reachable in n steps means reachable in n +- 2 steps

part1 = len(reachable_in[64])

steps = 26501365
n = 26501365 // 131 # assumes steps = 65 + 262k for some integer k
odd_squares = (n + 1)**2
even_squares = n**2
odd_corner_tiles = n + 1
even_corner_tiles = n

part2 = (
    odd_squares * len(reachable_in[131]) + 
    even_squares * len(reachable_in[130]) - 
    odd_corner_tiles * len(reachable_in[131] - reachable_in[65]) +
    even_corner_tiles * len(reachable_in[130] - reachable_in[64]))

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=21, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=21, year=2023)
