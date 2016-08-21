def main():
    with open('A-large.in') as data:
        test_cases = int(data.readline())
        for idx, line in enumerate(data):
            last_number = get_sleep(line)
            print('Case #{}: {}'.format(idx + 1, last_number))


def get_sleep(line):
    number = int(line.strip())
    if number == 0:
        return 'INSOMNIA'
    counter = 2
    current = number

    digits = set(str(current))
    while(len(digits) < 10):
        current = number * counter
        counter += 1
        digits = digits.union(str(current))

    return current

if __name__ == '__main__':
    main()
