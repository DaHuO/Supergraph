def process(n):
    # original_n = n
    # # eliminate trailing zeroes
    # while n % 10 == 0:
    #     if n == 0:
    #         return -1
    #     else:
    #         n /= 10

    if n == 0:
        return -1

    m = 1
    s = set()

    all_digits_seen = False
    while not all_digits_seen:
        r = original_r = m*n

        while r != 0:
            r, extracted_digit = divmod(r, 10)
            s.add(extracted_digit)

        all_digits_seen = len(s) == 10
        m += 1

    return original_r

number_of_cases = int(raw_input())
for case_number in xrange(1, number_of_cases+1):
    n = int(raw_input())

    result = process(n)
    if result == -1:
        result = 'INSOMNIA'

    print "Case #%d: %s" % (case_number, result)
    case_number += 1

# print process(0) == -1
# print process(1) == 10
# print process(2) == 90
# print process(11) == 110
# print process(1692) == 5076
# print process(10) == 90
