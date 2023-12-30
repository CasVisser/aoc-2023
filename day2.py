import aocd, sys

inp = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=2, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

R = 12
G = 13
B = 14

lines = inp.split("\n")

part1 = 0
part2 = 0

for i, game in enumerate(lines): 
    r = 0
    g = 0
    b = 0
    prefix = game.find(":")
    sets = game[prefix+2:].split("; ")
    for s in sets:
        piles = s.split(", ")
        for p in piles:
            n, c = p.split(" ")
            if c[0] == "r":
                r = max(r, int(n))
            elif c[0] == "g":
                g = max(g, int(n))
            else:
                b = max(b, int(n))
    if r <= R and g <= G and b <= B:
        part1 += i + 1
    part2 += r * g * b

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=2, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=2, year=2023)
