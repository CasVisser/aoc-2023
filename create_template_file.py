import os, sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python create_template_file.py <year> <day>")
        return
    
    year = sys.argv[1]
    day  = sys.argv[2]

    file_path = f"day{day}.py"
    if os.path.isfile(file_path):
        print(f"File already exists: \"{file_path}\"")
        return
    
    # The actual template. The inp on line 3 can be used to try example inputs
    template = (
f"""import aocd, sys

inp = r\"\"\"\"\"\"

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day={day}, year={year})

part1 = None
part2 = None

### BEGIN SOLUTION



### END SOLUTION

print(f"Part 1: {{part1}}")
print(f"Part 2: {{part2}}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day={day}, year={year})
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day={day}, year={year})
""")
    
    with open(f"day{day}.py", "w") as f:
        f.write(template)

if __name__ == "__main__":
    main()
