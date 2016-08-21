

def main():
    file = open('A-large.in', 'rU')
    lines = iter(file.readlines())
    file.close()

    cases_count = int(next(lines))

    output = open('output', 'w')
    for case_idx in range(cases_count):
        number = int(next(lines))

        if number == 0:
            print('Case #{}: INSOMNIA'.format(case_idx + 1), file=output)
            continue

        digits = set(str(number))
        next_number = number

        while len(digits) < 10:
            next_number += number
            digits = digits.union(str(next_number))

        print('Case #{}: {}'.format(case_idx + 1, next_number), file=output)

    output.close()


if __name__ == '__main__':
    main()
