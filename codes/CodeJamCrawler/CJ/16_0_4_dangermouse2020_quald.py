"""Qualification round - problem A"""

FILE_BASE = "D-small-attempt0"


def read_file():
    """reads file into list of puzzles"""
    with open(FILE_BASE + ".in") as file:
        cases = int(file.readline())
        puzzles = []
        for _ in range(cases):
            puzzles.append(tuple(int(i) for i in file.readline().split(" ")))
        return puzzles


def write_file(results):
    """writes results to file"""
    with open(FILE_BASE + ".out", "w+") as file:
        row = 1
        for result in results:
            file.write("Case #{0}: {1}\n".format(row, result))
            row += 1


def solve(puzzle):
    """solve single puzzle"""
    k = puzzle[0]
    c = puzzle[1]
    solution = tuple(range(1,k + 1))
    return " ".join((str(i) for i in solution))




PUZZLES = read_file()
RESULTS = [solve(puzzle) for puzzle in PUZZLES]

write_file(RESULTS)

