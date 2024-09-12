import aocd, sys

inp = r""""""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=20, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

from collections import defaultdict
from math import prod

mod_outs = defaultdict(list)
mod_ins  = defaultdict(list)
mod_type = defaultdict(lambda: "")
ff_state = defaultdict(lambda: 0)
conj_state = defaultdict(lambda: defaultdict(lambda: 0))
for line in inp.split("\n"):
    type_name, destinations = line.split(" -> ")
    destinations = destinations.split(", ")
    if type_name == "broadcaster": t = name = "broadcaster"
    else: t, name = type_name[0], type_name[1:]
    for d in destinations: mod_ins[d].append(name)
    mod_outs[name] = list(destinations)
    mod_type[name] = t    

first_turned_on = defaultdict(lambda: 1e10)
counts = [0, 0]
n_button_pushed = 0
while len(first_turned_on) < len(conj_state) - 1 or n_button_pushed < 1000:
    q = [(0, "button", "broadcaster")] # signal (0 is low, 1 is high), src, dst
    n_button_pushed += 1
    while len(q) > 0:
        sig, src, cur = q.pop(0)
        counts[sig] += 1
        match mod_type[cur]:
            case "broadcaster": 
                new_sig = sig
            case "%":
                if sig == 0: new_sig = ff_state[cur] = (ff_state[cur] + 1) % 2
                else: continue
            case "&":
                conj_state[cur][src] = sig
                new_sig = any(conj_state[cur][mod_in] == 0 for mod_in in mod_ins[cur])
                if not new_sig: first_turned_on[cur] = min(first_turned_on[cur], n_button_pushed)
        
        for dst in mod_outs[cur]: q.append((new_sig, cur, dst))
    if n_button_pushed == 1000: part1 = counts[0] * counts[1]

part2 = prod(first_turned_on.values())

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=20, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=20, year=2023)
