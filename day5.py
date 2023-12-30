import aocd, sys

inp = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=5, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

seeds = list(map(int, inp.split("\n\n")[0].split(": ")[1].split(" ")))
maps = []

for map_str in inp.split("\n\n")[1:]:
    m = []
    for line in map_str.split("\n")[1:]:
        dest, src, map_range = tuple(map(int, line.split(" ")))
        m.append((src, dest, map_range))
    maps.append(sorted(m))

def apply_maps(ranges):
    for m in maps:
        new_ranges = []
        for start, end in ranges:
            for src, dest, map_range in m:
                if src + map_range <= start:
                    continue
                if src > start:
                    new_start = min(end, src)
                    new_ranges.append((start, new_start))
                    start = new_start
                    if start == end:
                        break
                overlap_end = min(end, src + map_range)
                new_ranges.append((dest + start - src, dest + overlap_end - src))
                start = overlap_end
                if start == end:
                    break
            else:
                new_ranges.append((start, end))
        ranges = new_ranges
    return ranges

part1 = min(r[0] for r in apply_maps([(seed, seed + 1) for seed in seeds]))
part2 = min(r[0] for r in apply_maps([(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]))

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=5, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=5, year=2023)
