num_test_cases = 0
file_in = 'sheep_sm.in'


def print_case(case, result):
    print 'Case #%d: %s' % (case, result)


def get_inputs(input_string):
    global num_test_cases

    test_cases = input_string.split('\n')
    num_test_cases = int(test_cases[0])

    return [int(test_case) for test_case in test_cases[1:]]


def evaluate_input(case_input):
    solution = {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1,
                '8': 1, '9': 1}
    digits = {}
    if case_input == 0:
        return 'INSOMNIA'
    else:
        n = case_input
        current_num = 0

        while digits != solution:
            current_num += n

            for digit in str(current_num):
                digits.update({digit: 1})

        return current_num


def main():
    with file(file_in) as fin:
        str_input = ''.join(fin.readlines()).strip()

    inputs = get_inputs(str_input)

    with file(file_in.replace('in', 'out'), 'w+') as fout:
        for i in xrange(num_test_cases):
            result = evaluate_input(inputs[i])
            print_case(i + 1, result)
            fout.write('Case #%d: %s\n' % (i+1, result))


if __name__ == '__main__':
    main()
