

LETTERS = {
    0: "ZERO",
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE"
}


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
    number = ""
    digits_dict = calculate_digits(case)
    for d in digits_dict:
        number += str(d) * digits_dict[d]
    return number


def calculate_digits(s):
    d = {}
    l_count = s.count("Z")
    d[0] = l_count
    for c in LETTERS[0]:
        s = s.replace(c, "", l_count)
    l_count = s.count("X")
    d[6] = l_count
    for c in LETTERS[6]:
        s = s.replace(c, "", l_count)
    l_count = s.count("W")
    d[2] = l_count
    for c in LETTERS[2]:
        s = s.replace(c, "", l_count)
    l_count = s.count("U")
    d[4] = l_count
    for c in LETTERS[4]:
        s = s.replace(c, "", l_count)
    l_count = s.count("G")
    d[8] = l_count
    for c in LETTERS[8]:
        s = s.replace(c, "", l_count)
    l_count = s.count("R")
    d[3] = l_count
    for c in LETTERS[3]:
        s = s.replace(c, "", l_count)
    l_count = s.count("O")
    d[1] = l_count
    for c in LETTERS[1]:
        s = s.replace(c, "", l_count)
    l_count = s.count("F")
    d[5] = l_count
    for c in LETTERS[5]:
        s = s.replace(c, "", l_count)
    l_count = s.count("S")
    d[7] = l_count
    for c in LETTERS[7]:
        s = s.replace(c, "", l_count)
    l_count = s.count("I")
    d[9] = l_count
    for c in LETTERS[9]:
        s = s.replace(c, "", l_count)
    return d


def main():
    # path = r"C:\Users\User\Downloads\A-small-attempt0.in"
    res = ""
    case_counter, cases = read_input()
    for i in xrange(int(case_counter)):
        case = cases[i]
        case_result = handle_case(case)
        res += "Case #{}: {}\n".format((i + 1), case_result)

    print res[:-1],
    # write_res(path + ".out", res[:-1])

if __name__ == '__main__':
    main()
