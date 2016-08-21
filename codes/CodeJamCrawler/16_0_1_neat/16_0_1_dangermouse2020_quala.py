"""Qualification round - problem A"""

FILE_BASE = "A-large"

def read_file():
    """reads file into list of puzzles"""
    with open(FILE_BASE + ".in") as file:
        cases = int(file.readline())
        puzzles = []
        for _ in range(cases):
            puzzles.append(int(file.readline()))
        return puzzles


def write_file(results):
    """writes results to file"""
    with open(FILE_BASE + ".out", "w+") as file:
        row = 1
        for result in results:
            file.write("Case #{0}: {1}\n".format(row, result))
            row += 1

def solve(number):
    """solve single puzzle"""
    if number == 0:
        return "INSOMNIA"
    else:
        seen_digits = set()
        i = 1
        n = 0
        while len(seen_digits) < 10:
            n = number * i
            seen_digits = seen_digits.union(digits(n))
            i += 1
        return n


def digits(number):
    """set of digits for given number"""
    return set([int(i) for i in str(number)])


print(solve(0))
print(solve(1))
print(solve(2))
print(solve(11))
print(solve(1692))

PUZZLES = read_file()
RESULTS = [solve(number) for number in PUZZLES]

write_file(RESULTS)

