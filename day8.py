import aocd, sys

# inp = """RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)"""

# inp = """LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)"""

inp = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=8, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

from math import lcm

instructions, lines = inp.split("\n\n")
m = {line[:3]: (line[7:10], line[12:15]) for line in lines.split("\n")}

def cycle_time(pos):
    seen = {(pos, n := 0): n}
    while True:
        ins = 0 if instructions[n % len(instructions)] == "L" else 1
        pos = m[pos][ins]
        n += 1
        if (pos, n % len(instructions)) in seen:
            return n - seen[pos, n % len(instructions)]
        seen[pos, n % len(instructions)] = n

part1 = cycle_time("AAA")

start_positions = [node for node in m if node[-1] == "A"]
cycle_times = [cycle_time(pos) for pos in start_positions]
part2 = lcm(*cycle_times)

### END SOLTUION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=8, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=8, year=2023)
