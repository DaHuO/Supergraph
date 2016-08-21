def iterate(filename):
    fileling = open(filename)
    num_cases = int(fileling.readline())
    for case_num in range(num_cases):
        number = int(fileling.readline())
        print "Case #" + str(case_num + 1) + ':', process(number)


def process(number):
    if number == 0:
        return 'INSOMNIA'
    numbers = set()
    current = res = number
    multiple = 2
    while len(numbers) < 10:
        # print number, numbers
        str_num = str(current)
        for char in str_num:
            numbers.add(char)
        res = current
        current = number * multiple
        multiple += 1
    return res


if __name__ == '__main__':
    iterate('A-large.in')
