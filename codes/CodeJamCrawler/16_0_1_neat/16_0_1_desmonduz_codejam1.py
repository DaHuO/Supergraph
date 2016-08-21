def main(file_name):
    with open(file_name, 'r') as f:
        case_count = int(f.readline())
        output = []
        for case in range(case_count):
            output.append("Case #%s: %s" % (case + 1, solve(int(f.readline()))))
        return output


def solve(num):
    prev_digits = digits = set(split_digits(num))
    coefficient = 2
    failed = 0
    while len(digits) < 10:
        if failed > 100:
            return "INSOMNIA"
        new_num = num * coefficient
        new_digits = set(split_digits(new_num))
        if len(new_digits ^ prev_digits) == 0:
            failed += 1
        else:
            failed = 0
        digits.update(new_digits)
        prev_digits = new_digits
        coefficient += 1
    return str(new_num)


def split_digits(num):
    return list(str(num))

if __name__ == '__main__':
    file_name = 'A-large.in'
    output = main(file_name)
    output = "\n".join(output)
    print output
    with open("output5.txt", "w") as f:
        f.write(output)
