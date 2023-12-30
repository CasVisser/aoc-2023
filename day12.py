import aocd, sys

inp = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=12, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

import itertools
import functools

@functools.lru_cache(maxsize=None)
def n_alternatives(record, groups):
    if len(groups) == 0 and "#" not in record:
        return 1
    if (len(groups) == 0 and "#" in record) or (sum(groups) > record.count("#") + record.count("?")):
        return 0
    if record[0] == ".":
        return n_alternatives(record[1:], groups)
    res = 0 # next char is either # or ?
    if "." not in record[:groups[0]] and (len(record) == groups[0] or record[groups[0]] != "#"):
        res += n_alternatives(record[groups[0] + 1:], groups[1:]) # try ? is #
    if record[0] == "?":
        res += n_alternatives(record[1:], groups) # try ? is .    
    return res

lines = inp.split("\n")
part1 = part2 = 0
for line in lines:
    record, groups = line.split(" ")
    part1 += n_alternatives(record, groups := tuple(map(int, groups.split(","))))
    part2 += n_alternatives("?".join(itertools.repeat(record, 5)), 5 * groups)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=12, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=12, year=2023)

# for line in lines:
#     record, groups = line.split(" ")
#     groups = list(map(int, groups.split(",")))
#     missing_indexes = [i for i, r in enumerate(record) if r == "?"]
#     def valid(replacements):
#         fixed_record = list(record)
#         for i, replacement in zip(missing_indexes, replacements): fixed_record[i] = replacement
#         fixed_record_groups = [len(list(group)) for c, group in itertools.groupby(fixed_record) if c == "#"]
#         return fixed_record_groups == groups
#     part1 += len(list(filter(valid, itertools.product("#.", repeat=len(missing_indexes)))))