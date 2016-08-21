import sys
sys.path.append("/Users/jevenson/pers/pers/googlecode")
import base

FAIL_SETS = [set(['0'])]

def getDigits(number):
    return set([s for s in str(number)])

def solve(problem):
    """
    @problem: (list of list of int) a list where each item is one of the
      lines in the problem. Each item is also a list, of each number in
      the line parsed and separated

    @return: (str) the solution to be printed
    """
    assert len(problem) == 1
    base = problem[0]

    if getDigits(base) in FAIL_SETS:
        return "INSOMNIA"

    current = base
    seen = set()
    i = 1
    while True:
        seen.update(getDigits(current))
        if len(seen) > 9:
            return current
        i += 1
        current = base * i

if __name__ == "__main__":
    base.main(solve)
