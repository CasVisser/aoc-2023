import aocd, sys

inp = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=9, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

from collections import deque

def differences(l):
    return deque(l[i + 1] - l[i] for i in range(len(l) - 1))

part1 = 0
part2 = 0
for line in inp.split("\n"):
    difference_lists = [deque(map(int, line.split()))] # start with just the numbers
    while not all(map(lambda x: x == 0, difference_lists[-1])):
        difference_lists.append(differences(difference_lists[-1]))
    difference_lists[-1].append(0)
    difference_lists[-1].appendleft(0)
    for i in range(len(difference_lists) - 1, 0, -1):
        difference_lists[i - 1].append(difference_lists[i - 1][-1] + difference_lists[i][-1])
        difference_lists[i - 1].appendleft(difference_lists[i - 1][0] - difference_lists[i][0])
    part1 += difference_lists[0][-1]
    part2 += difference_lists[0][0]

### END SOLTUION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=9, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=9, year=2023)
