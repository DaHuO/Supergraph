

def read_input():
    line_numbers = int(raw_input())  # read a line with a single integer
    lines = []
    for i in xrange(1, line_numbers + 1):
        lines.append(raw_input())
    return line_numbers, lines


def handle_case(case):
    count = 0
    last_seen = ""
    for i in case:
        if i != last_seen:
            count += 1
            last_seen = i
    if last_seen == "+":
        count -= 1
    return count


def main():
    res = ""
    case_counter, cases = read_input()
    for i in xrange(int(case_counter)):
        case = cases[i]
        case_result = handle_case(case)
        res += "Case #{}: {}\n".format((i + 1), case_result)

    print res[:-1]

if __name__ == '__main__':
    main()
