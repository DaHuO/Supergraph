def find_asleep_number(number):
    if number == '0':
        return "INSOMNIA"
    digits = set(number)
    m = 2
    checked_number = number
    while True:
        if len(digits) == 10:
            return number
        number = str(int(checked_number) * m)
        digits |= set(number)
        m += 1


def print_solutions(filename):
    content = open(filename).read().strip().split('\n')
    test_case_count = int(content[0])
    i = 1
    while i <= test_case_count:
        number = find_asleep_number(content[i])
        print("Case #%s: %s" % (i, number))
        i += 1

filename = raw_input()
print_solutions(filename)
