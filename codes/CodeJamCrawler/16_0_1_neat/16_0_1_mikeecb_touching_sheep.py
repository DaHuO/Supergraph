
test_cases = int(raw_input())

for test_case in xrange(test_cases):

    i = 1
    n = int(raw_input())
    seen_digits = set()

    if n is 0:
        print 'Case #' + str(test_case + 1) + ': INSOMNIA'
        continue

    while len(seen_digits) < 10:
    
        current_n = i * n
        i += 1

        for digit in str(current_n):
            seen_digits.update(digit)

    print "Case #" + str(test_case + 1) + ": " + str(current_n)
