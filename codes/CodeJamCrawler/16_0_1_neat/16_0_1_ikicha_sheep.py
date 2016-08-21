def get_digits(n):
    str_n = str(n)
    result = []
    for i in range(0, len(str_n)):
        result.append(int(str_n[i]))
    return result


def solve(n):
    if n == 0:
        return "INSOMNIA"
    digits = []
    for i in range(0, 10):
        digits.append(i)
    idx = 0
    current = 0
    while len(digits) > 0:
        current = n * (idx + 1)
        for i in get_digits(current):
            if i in digits:
                digits.remove(i)
        idx += 1
    return str(current)


def main():
    with open("A-input.in") as fin:
        with open("A-output.out", "w") as fout:
            n = int(fin.readline())
            for i in range(0, n):
                fout.write("Case #%d: %s\n" % (i + 1, solve(int(fin.readline()))))


main()

