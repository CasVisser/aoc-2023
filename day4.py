import aocd, sys

inp = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=4, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

cards = inp.split("\n")

def parse_card(card):
    numbers = list(filter(lambda x: len(x) > 0, card.split(": ")[1].split(" ")))
    split = numbers.index("|")
    return set(map(int, numbers[:split])), set(map(int, numbers[split + 1:]))

part1 = 0
part2 = len(cards)
multiplier = [1] * len(cards)
for i, c in enumerate(cards):
    winning, have = parse_card(c)
    n_have_in_winning = len(have.intersection(winning))
    part1 += int(2 ** (n_have_in_winning - 1))
    for j in range(i + 1, i + 1 + n_have_in_winning): multiplier[j] += multiplier[i]
    part2 += multiplier[i] * n_have_in_winning

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=4, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=4, year=2023)
