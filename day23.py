import aocd, sys

inp = r"""#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=23, year=2023)

part1 = None
answer = None

### BEGIN SOLUTION

from collections import defaultdict
from tqdm import tqdm

# Parse input
grid = {complex(i, j): c # grid[row + column*j] is . or > or ^ or ...
        for i, line in enumerate(inp.split()) 
        for j, c in enumerate(line)
        if c != "#"}
start = 0 + 1j
goal = complex(inp.count("\n"), inp.index("\n") - 2)

def get_all_neighbors(pos):
    return {pos + d for d in [1, -1, 1j, -1j] if pos + d in grid}

# Use for part 1
def get_neighbors(pos):
    return {pos + d for d, c in [(1, "v"), (-1, "^"), (1j, ">"), (-1j, "<")]
            if pos + d in grid and grid[pos + d] in [".", c]}

# Use for part 2
# def get_neighbors(pos):
#     return get_all_neighbors(pos)

# A successor is a junction (or the goal)
def get_successors(pos):
    seen = {pos}
    successors = set()
    q = {(n, 1) for n in get_neighbors(pos)}
    while q:
        cur, d = q.pop()
        if cur == goal:
            successors.add((cur, d))
            continue
        neighbors = get_all_neighbors(cur) - seen
        if len(neighbors) == 0: # ignore dead ends
            continue
        if len(neighbors) == 1: # not a junction
            seen.add(cur) # prevent walking back
            q.add((neighbors.pop(), d + 1))
            continue
        successors.add((cur, d)) # junction found!
    return successors

# Construct graph
graph = defaultdict(lambda: defaultdict(int))
q = {start}
seen = {start}
while q:
    cur = q.pop()
    for successor, d in get_successors(cur):
        graph[cur][successor] = max(graph[cur][successor], d)
        if successor not in seen:
            q.add(successor)
            seen.add(successor)

# BFS
q = [(start, set(), 0)]
answer = 0
while q:
    cur, cur_seen, d = q.pop()
    for succ in graph[cur]:
        if succ in cur_seen:
            continue
        if succ == goal:
            answer = max(answer, d + graph[cur][succ])
            continue
        q.append((succ, set(cur_seen) | {cur}, d + graph[cur][succ]))

### END SOLUTION

print(f"Answer: {answer}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(answer, part="a", day=23, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(answer, part="b", day=23, year=2023)
