all_digits = set(digit for digit in range(0, 10))

case_count = int(raw_input())
for case_number in xrange(1, case_count + 1):
    n = int(raw_input())

    result = "INSOMNIA"
    if n != 0:
        seen_digits = set()
        for i in xrange(1, 101):
            next_number = i * n
            for digit in str(next_number):
                seen_digits.add(int(digit))
            if all_digits == seen_digits:
                result = next_number
                break

    print "Case #{}: {}".format(case_number, result)
