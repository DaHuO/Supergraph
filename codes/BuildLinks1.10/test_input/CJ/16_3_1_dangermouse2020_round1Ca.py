"""Round 1C - problem A"""

import string

FILE_BASE = "A-large"
alphabet_lookup = dict(zip(range(26), string.ascii_lowercase))


def read_file():
    """reads file into list of puzzles"""
    with open(FILE_BASE + ".in") as file:
        cases = int(file.readline())
        puzzles = []
        for _ in range(cases):
            num_parties = int(file.readline())
            puzzles.append([int(x) for x in file.readline().strip().split(" ")])
        return puzzles


def write_file(results):
    """writes results to file"""
    with open(FILE_BASE + ".out", "w+") as file:
        row = 1
        for result in results:
            result_str = " ".join(result)
            file.write("Case #{0}: {1}\n".format(row, result_str))
            row += 1


def solve(puzzle):
    """solve single puzzle"""
    maxi = max(puzzle)
    if maxi == 0:
        return []
    else:
        max_index = puzzle.index(maxi)
        puzzle[max_index] = maxi - 1
        alpha = alphabet_lookup[max_index]
        if maxi in puzzle and (maxi > 1 or sum(puzzle) == 1):
            second_index = puzzle.index(maxi)
            puzzle[second_index] = maxi - 1
            beta = alphabet_lookup[second_index]
            return [alpha + beta] + solve(puzzle)
        else:
            return [alpha] + solve(puzzle)


print(solve([1, 1]))
print(solve([2, 2]))
print(solve([3, 2, 2]))
print(solve([1, 1, 2]))
print(solve([2, 3, 1]))

PUZZLES = read_file()
RESULTS = [solve(puzzle) for puzzle in PUZZLES]
write_file(RESULTS)
