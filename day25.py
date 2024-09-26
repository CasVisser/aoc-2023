import aocd, sys

inp = r"""jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=25, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

from collections import defaultdict, deque

g = defaultdict(set)
for line in inp.split("\n"):
    src, dests = line.split(": ")
    dests = dests.split(" ")
    g[src] |= set(dests)
    for d in dests:
        g[d].add(src)

def get_distinct_path(src, dst, used_edges):
    seen = set()
    q = deque([(src, used_edges)])
    while q:
        cur, used = q.popleft()
        if cur in seen:
            continue
        seen.add(cur)
        if cur == dst:
            return used
        for neighbor in g[cur]:
            if neighbor in seen:
                continue
            edge = frozenset((cur, neighbor))
            if edge not in used:
                q.append((neighbor, used | {edge}))
    return None

nodes = list(g.keys())
src = nodes[0]
part1 = 1
for dst in nodes[1:]:
    n_distinct_paths = 0
    used = set()
    while (new_used := get_distinct_path(src, dst, used)):
        used |= new_used
        n_distinct_paths += 1
    if n_distinct_paths > 3:
        part1 += 1

part1 *= len(nodes) - part1

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=25, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=25, year=2023)
