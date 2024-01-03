import aocd, sys

inp = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=18, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

def get_volume(instructions):
    trench_size = 0
    pos = 0
    points = [pos]
    for d, n_steps in instructions:
        trench_size += n_steps
        pos += n_steps * d
        points.append(pos)
    return int((abs(sum(points[i].real * (points[(i + 1)].imag - points[i - 1].imag) 
                for i in range(-1, len(points) - 1))) + trench_size) / 2) + 1

dig_plan = list(map(str.split, inp.split("\n")))
name_to_d = {"R": 1j, "D": 1, "L": -1j, "U": -1}
wrong_instructions = [(name_to_d[d], int(n_steps)) for d, n_steps, _ in dig_plan]
corrected_instructions = [(list(name_to_d.values())[int(ins[-2])], int(ins[2:-2], 16)) for _, _, ins in dig_plan]
part1 = get_volume(wrong_instructions)
part2 = get_volume(corrected_instructions)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=18, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=18, year=2023)
