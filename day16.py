import aocd, sys

inp = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=16, year=2023)

part1 = None
part2 = None

### BEGIN SOLUTION

grid = inp.split("\n")

def get_start_beams():
    n_rows = len(grid)
    n_cols = len(grid[0])
    start_beams = set()
    for row in range(n_rows):
        start_beams.add(((row, -1),     (0,  1)))
        start_beams.add(((row, n_cols), (0, -1)))
    for col in range(n_cols):
        start_beams.add(((-1, col),     ( 1, 0)))
        start_beams.add(((n_cols, col), (-1, 0)))
    return start_beams

def n_energized(start_beam):
    q = [start_beam] # ((row, col), (d_row, d_col))
    seen = set(q)
    energized = set()
    while len(q) > 0:
        (row, col), (d_row, d_col) = q.pop(0)
        new_row, new_col = row + d_row, col + d_col
        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])): continue

        if grid[new_row][new_col] == "/":
            new_beams = [((new_row, new_col), (-d_col, -d_row))]
        elif grid[new_row][new_col] == "\\":
            new_beams = [((new_row, new_col), (d_col, d_row))]
        elif grid[new_row][new_col] == "-" and d_row != 0:
            new_beams = [((new_row, new_col), (0, 1)), ((new_row, new_col), (0, -1))]
        elif grid[new_row][new_col] == "|" and d_col != 0:
            new_beams = [((new_row, new_col), (1, 0)), ((new_row, new_col), (-1, 0))]
        else:
            new_beams = [((new_row, new_col), (d_row, d_col))]
        
        for beam in new_beams:
            if beam not in seen: 
                q.append(beam)
                energized.add(beam[0])
                if grid[beam[0][0]][beam[0][1]] in "-|": seen.add(beam)
    
    return len(energized)

part1 = n_energized(((0, -1), (0, 1)))
part2 = max(n_energized(((start_row, start_col), (start_d_row, start_d_col)))
        for (start_row, start_col), (start_d_row, start_d_col) in get_start_beams())

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=16, year=2023)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=16, year=2023)
