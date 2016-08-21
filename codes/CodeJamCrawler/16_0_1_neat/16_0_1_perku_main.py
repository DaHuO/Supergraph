def reader(input_file):
    with open(input_file) as f:
        len_cases = int(f.readline())
        numbers = []
        for case in xrange(len_cases):
            numbers.append(int(f.readline()))
    return numbers


def solver(number):
    distribution = {i: False for i in xrange(10)}
    n = number
    i = 2
    while True:
        for digit in str(number):
            distribution[int(digit)] = True
        if len(set(distribution.values())) == 1:
            return number
        number = n * i
        i += 1
        if i == 500:
            return 'INSOMNIA'


numbers = reader('large.in')
for idx, number in enumerate(numbers):
    result = solver(number)
    print 'Case #{}: {}'.format(idx+1, result)
