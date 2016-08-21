INPUT_FILENAME = 'large-input.txt'
OUTPUT_FILENAME = 'large-output.txt'

def get_digits(integer):
    """
    Returns a list of all the digits in the given integer.

    Example:
        1234 -> [1, 2, 3, 4]
    """
    integer_string = str(integer)
    set = []
    for char in integer_string:
        set.append(int(char))
    return set


def main():
    assert [i in get_digits(1234) for i in [1, 2, 3, 4]]

    # Get test cases from input file
    test_cases = []
    with open(INPUT_FILENAME, 'r') as f:
        num_test_cases = int(f.readline())
        for line in f.readlines():
            test_cases.append(int(line))
        assert num_test_cases == len(test_cases), '%s != %s' % (num_test_cases, len(test_cases))

    # Increment through each test case
    results = []
    for test_case in test_cases:
        if test_case == 0:
            results.append('INSOMNIA')
            continue
        i = 0  # We increment first, so we start by checking 1
        case_set = set()
        while True:
            i += 1
            value_for_this_iteration = test_case * i
            digits_in_number = get_digits(value_for_this_iteration)
            for digit in digits_in_number:
                case_set.add(digit)
            if len(case_set) >= 10:
                results.append(value_for_this_iteration)
                break

    with open(OUTPUT_FILENAME, 'w') as f:
        for i, res in enumerate(results):
            f.write('Case #%s: %s\n' % (i + 1, res))


if __name__ == '__main__':
    main()
