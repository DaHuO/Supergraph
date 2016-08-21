def get_digits(number):
    digits = set()
    while number:
        digits.add(number % 10)
        number /= 10

    return digits


for case_num in xrange(int(raw_input())):
    num = int(raw_input())
    cache = set()
    start = 0

    if num == 0:
        print 'Case #{}: {}'.format(case_num + 1, 'INSOMNIA')
        continue

    while True:
        start += num
        for digit in get_digits(start):
            cache.add(digit)

        if len(cache) == 10:
            print 'Case #{}: {}'.format(case_num + 1, start)
            break
