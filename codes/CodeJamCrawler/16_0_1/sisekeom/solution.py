"SOlution for a CodeJam 2016 poblem"
import sys

LINES_PER_CASE = 1


def _get_ciphers(number):
    ciphers = []
    while number is not 0:
        ciphers.append(number % 10)
        number = number // 10
    return set(ciphers)


def run_problem(test):
    test = int(test[0])

    if test == 0:
        return "INSOMNIA"

    numbers = list(range(10))
    index = 1
    while numbers:
        mult = index * test
        ciphers = _get_ciphers(mult)
        for num in ciphers:
            try:
                numbers.remove(num)
            except Exception:
                continue
        index = index + 1
    return mult


def _output(results):
    with open("output.txt", "w") as f_out:
        for index, result in enumerate(results):
            f_out.write("Case #{}: {}\n".format(index + 1, result))


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
