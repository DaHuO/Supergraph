
def handle_input(path):
    lines = open(path, "rb").readlines()
    return int(lines[0]), lines[1:]


def read_input():
    line_numbers = int(raw_input())  # read a line with a single integer
    lines = []
    for i in xrange(1, line_numbers + 1):
        lines.append(raw_input())
    return line_numbers, lines

def write_res(path, results):
    result_file = file(path, "wb")
    result_file.write(results)


def handle_case(case):
    digits_seen = [0] * 10

    base_number = int(case)
    last_number = 0
    if base_number == 0:
        return "INSOMNIA"
    while 0 in digits_seen:
        last_number += base_number
        digits = get_digits(last_number)
        for dig in digits:
            digits_seen[dig] += 1
    return last_number


def get_digits(number):
    digits = []
    while number:
        digits.append(number % 10)
        number /= 10
    return digits


def main():
    #path = r"C:\Users\User\Downloads\A-small-attempt0.in"
    res = ""
    case_counter, cases = read_input()
    for i in xrange(int(case_counter)):
        case = cases[i]
        case_result = handle_case(case)
        res += "Case #{}: {}\n".format((i + 1), case_result)

    print res[:-1],
    #write_res(path + ".out", res[:-1])

if __name__ == '__main__':
    main()
