import aocd, sys

inp = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=13, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

def reflection_score(lines):
    for i in range(len(lines) - 1):
        for d in range(min(i + 1, len(lines) - i - 1)):
            if lines[i - d] != lines[i + 1 + d]:
                break
        else:
            return i + 1
    return -1

def reflection_score2(lines):
    for i in range(len(lines) - 1):
        corrected_smudge = False
        for d in range(min(i + 1, len(lines) - i - 1)):
            diff = sum(lines[i - d][j] != lines[i + 1 + d][j] for j in range(len(lines[i - d])))
            if diff == 1 and not corrected_smudge:
                corrected_smudge = True
                continue
            if diff > 0:
                break
        else:
            if corrected_smudge: return i + 1
    return -1

patterns = inp.split("\n\n")
part1 = part2 = 0
for pattern in patterns:
    score1 = 100 * reflection_score(lines := pattern.split("\n"))
    if score1 < 0:
        score1 = reflection_score(list(zip(*reversed(lines))))
    part1 += score1

    score2 = 100 * reflection_score2(lines := pattern.split("\n"))
    if score2 < 0:
        score2 = reflection_score2(list(zip(*reversed(lines))))
    part2 += score2

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=13, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=13, year=2023)
