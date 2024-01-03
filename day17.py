import aocd, sys

inp = r"""2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=17, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

from heapq import heappush, heappop

grid = {(row_i, col_i): int(c) for row_i, row in enumerate(inp.split("\n"))
                               for col_i, c in enumerate(row)}
goal = list(grid.keys())[-1]

def heat_loss(min_steps, max_steps):
    q = [(0, (0, 0), (0, 1)), (0, (0, 0), (1, 0))] # state :: (loss, pos, dir)
    seen = set()
    while len(q) > 0:
        loss, pos, dir = heappop(q)
        if pos == goal: return loss
        if (pos, dir) in seen: continue
        seen.add((pos, dir))

        for new_dir in [(-dir[1], dir[0]), (dir[1], -dir[0])]: # left turn, right turn
            for n_steps in range(min_steps, max_steps + 1):
                new_pos = (pos[0] + n_steps * new_dir[0], pos[1] + n_steps * new_dir[1])
                if new_pos not in grid: break
                new_loss = loss + sum(grid[pos[0] + n * new_dir[0], pos[1] + n * new_dir[1]] for n in range(1, n_steps + 1))
                heappush(q, (new_loss, new_pos, new_dir))

part1 = heat_loss(1, 3)
part2 = heat_loss(4, 10)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=17, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=17, year=2023)
