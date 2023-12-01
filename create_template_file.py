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
    
    template = (
f"""import aocd

inp = aocd.get_data(day={day}, year={year})



part1 = 

print(part1)
# print(aocd.submit(part1, part="a", day={day}, year={year}))

# part2 = 
# print(part2)
# print(aocd.submit(part2, part="b", day={day}, year={year})""")
    
    with open(f"day{day}.py", "w") as f:
        f.write(template)

if __name__ == "__main__":
    main()
