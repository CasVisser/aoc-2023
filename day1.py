import aocd

inp = aocd.get_data(day=1, year=2023)

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

part1 = []
part2 = []

for l in inp.split("\n"):
    lmost = len(l)
    rmost = 0
    ld = -1
    rd = -1

    digits = [c for c in l if c.isnumeric()]
    part1.append(int("".join([digits[0], digits[-1]])))

    for s, r in str_digit:
        lpos, rpos = l.find(s), l.rfind(s)
        if lpos != -1 and lpos <= lmost:
            lmost = lpos
            ld = r
        if rpos != -1 and rpos >= rmost:
            rmost = rpos
            rd = r
    
    part2.append(10 * ld + rd)
    
print(sum(part1))
print(sum(part2))
