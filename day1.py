import aocd

# inp = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen"""

inp = aocd.get_data(day=1, year=2023)

numbers = []

# for l in inp.split("\n"):
#     print(l)
#     n = [c for c in l if c.isnumeric()]
#     numbers.append(int("".join([n[0], n[-1]])))
    
# part1 = sum(numbers)
# print(part1)
# print(aocd.submit(part1, part="a", day=1, year=2023))

str_digit = [
    ("0", 0),
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
    ("6", 6),
    ("7", 7),
    ("8", 8),
    ("9", 9),
    ("zero", 0),
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9)]

for l in inp.split("\n"):
    lmost = len(l)
    rmost = 0
    ld = -1
    rd = -1
    for s, r in str_digit:
        pos = l.find(s)
        if pos != -1 and pos <= lmost:
            lmost = pos
            ld = r
        pos = l.rfind(s)
        if pos != -1 and pos >= rmost:
            rmost = pos
            rd = r

    numbers.append(10 * ld + rd)

print(numbers[-20:])

part2=sum(numbers)
print(part2)

aocd.submit(part2, part="b", day=1, year=2023)