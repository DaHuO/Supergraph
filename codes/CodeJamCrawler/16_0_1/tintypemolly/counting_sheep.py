def main():
    with open('A-large.in') as input_file, open('A-large.out', 'w') as result_file:
        case_count = int(input_file.readline().strip())
        for i in range(case_count):
            case_no = i + 1
            start_number = int(input_file.readline().strip())
            result = str(find_sleeping_number(start_number))
            result_file.write('Case #%d: %s\n' % (case_no, result))


def find_sleeping_number(start_number):
    if start_number == 0:
        return 'INSOMNIA'
    seen = set()
    mult = 1
    while len(seen) < 10:
        digits = get_digits(start_number * mult)
        seen.update(digits)
        mult += 1
    mult -= 1
    return start_number * mult


def get_digits(number):
    results = set()
    while number > 0:
        results.add(int(number % 10))
        number /= 10
    return results


if __name__ == "__main__":
    main()
