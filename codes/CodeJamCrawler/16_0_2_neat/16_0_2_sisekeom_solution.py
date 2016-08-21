"SOlution for a CodeJam 2016 poblem"
import sys

LINES_PER_CASE = 1


def _remove_leftmost_pluses(test):
    if test[-1] == "-":
        return test

    index = -1

    while test[index] == '+':
        index = index - 1

    return test[:index + 1]


def _count_groups(test):
    groups = [test[0]]

    for char in test:
        if groups[-1] is not char:
            groups.append(char)

    return len(groups)


def run_problem(test):
    "The actual code of the solution"
    test = test[0]
    if len(set(test)) == 1 and test[0] == "+":
        return 0
    test = _remove_leftmost_pluses(test)
    return _count_groups(test)


def _output(results):
    with open("output.txt", "w") as f:
        for index, result in enumerate(results):
            f.write("Case #{}: {}\n".format( index + 1, result))


def _read_args():
    "Gets the test cases for the current problem"
    number_of_cases = int(sys.stdin.readline().strip())
    test_cases = []
    for _ in range(number_of_cases):
        test_cases.append([])
        for _ in range(LINES_PER_CASE):
            test_cases[-1].append(sys.stdin.readline()[:-1])
    return test_cases


def main():
    "Entry point for the problem solver"
    results = []
    test_cases = _read_args()
    for test in test_cases:
        results.append(run_problem(test))
    _output(results)


if __name__ == "__main__":
    main()
