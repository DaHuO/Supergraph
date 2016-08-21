import math

def read_input():
    line_numbers = int(raw_input())  # read a line with a single integer
    lines = []
    for i in xrange(1, line_numbers + 1):
        lines.append(raw_input())
    return line_numbers, lines


BITS = ["1", "0"]
OPTIONS_LIST = []


def handle_case(case):
    digits_number = int(case.split(" ")[0]) - 2
    jamcoins_count = int(case.split(" ")[1])
    create_options(digits_number)
    options = OPTIONS_LIST[:]
    jamcoins_found = 0
    for option in options:
        actual_option = "1" + option + "1"
        bases = create_base_interpretation(actual_option)
        dividors_res = check_options(bases)
        if dividors_res:
            print "{} {}".format(actual_option, connect_list(dividors_res))
            jamcoins_found += 1
            if jamcoins_found == jamcoins_count:
                return


def create_options(n, past=""):
    if n == 0:
        OPTIONS_LIST.append(past)
        return
    create_options(n - 1, past + BITS[1])
    create_options(n - 1, past + BITS[0])


def create_base_interpretation(s):
    return [int(s, i) for i in xrange(2, 11)]


def check_options(base_interpretations):
    dividor_list = []
    for base_inter in base_interpretations:
        dividor = find_dividor(base_inter)
        if dividor == -1:
            return False
        else:
            dividor_list.append(dividor)
    return dividor_list


def find_dividor(n):
    for i in xrange(2, int(math.sqrt(n)) + 2):
        if n % i == 0:
            return i
    return -1


def connect_list(list_ints):
    strings = map(lambda x: str(x), list_ints)
    return " ".join(strings)


def main():
    case_counter, cases = read_input()
    for i in xrange(int(case_counter)):
        case = cases[i]
        print "Case #{}:".format(i + 1)
        handle_case(case)

if __name__ == '__main__':
    main()
