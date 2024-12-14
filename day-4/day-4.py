from collections import Counter
def import_input(run=True):
    if run:
        with open("./day-4/day-4-input.txt") as file:
            lines = [line.strip("/n") for line in file.readlines()]

    else:
        lines = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX"
        ]
    return lines

def create_grid(word_search):
    H, W = len(word_search), len(word_search[0])-1
    grid = {(y,x): word_search[y][x] for y in range(H) for x in range(W)}
    return grid

def find_xmas(letter_grid):
    TARGET = "XMAS"
    DELTAS =[(dy,dx) for dy in [-1,0,1] for dx in [-1,0,1] if (dx!=0 or dy!=0)]
    count = 0
    for y, x in letter_grid:
        for dy, dx in DELTAS:
            candidate = "".join(letter_grid.get((y+dy*i, x+dx*i),"") for i in range(len(TARGET)))
            count += candidate == TARGET
    print(f"XMAS Count: {count}")
    return count

def find_x_mas(letter_grid):
    DELTAS = [(dy, dx) for dy in [-1,1] for dx in [-1,1]]
    count = 0
    for y,x in letter_grid:
        candidate = letter_grid.get((y,x))
        for dy, dx in DELTAS:
            candidate += letter_grid.get((y+dy, x+dx),"")
        count += candidate == "AMSMS" or candidate == "ASSMM" or candidate == "AMMSS" or candidate == "ASMSM"

    print(f"X-MAS Count: {count}")
    return count


def main():
    word_search = import_input(run=True)
    letter_grid = create_grid(word_search=word_search)
    xmas_count = find_xmas(letter_grid=letter_grid)
    x_mas_count = find_x_mas(letter_grid=letter_grid)

main()