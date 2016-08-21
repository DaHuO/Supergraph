from itertools import count


def main():
    test_cases = parse_input()
    solutions = []
    for test_case in test_cases:
        solutions.append(solve(test_case))
    output_solutions(solutions)


def parse_input(path='input-large.in'):
    with open(path) as f:
        n = int(f.readline())
        test_cases = list(map(int, f.read().split()))
    assert n == len(test_cases)
    return test_cases


def output_solutions(solutions):
    with open('output', 'w') as f:
        for i, solution in enumerate(solutions, 1):
            f.write('Case #{i}: {result}\n'.format(
                    i=i,
                    result=solution if solution is not None else 'INSOMNIA'))


def solve(n):
    if n == 0:
        return None
    digits = set(range(10))
    for i in count(1):
        current_number = i * n
        current_digits = number_to_digits(current_number)
        digits.difference_update(current_digits)
        if not digits:
            return current_number


def number_to_digits(n):
    return set(int(digit) for digit in str(n))

if __name__ == '__main__':
    main()
