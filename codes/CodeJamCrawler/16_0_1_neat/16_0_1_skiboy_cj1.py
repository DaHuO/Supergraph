#!/usr/bin/python
import sys

# Part of 2016 Google code jam

# This task  counts from n, 2xn, 3xn until all 10 digits are represented in th results
def count_sheep(n):
    count = 1
    unfound_digits = {'0': 'x','1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x'}

    while count < 200:
        result = n * count
        digits = sorted(set(list(str(result))))

        for d in digits:
            if unfound_digits.has_key(d):
                del unfound_digits[d]

                if len(unfound_digits) == 0:
                    return result

        #print str(n) + ' * ' + str(count) + ' = ' + str(result) + ' unique: ' + str(digits) + ' remaining: ' + str(unfound_digits)

        count = count + 1

    return 'INSOMNIA'

T = int(raw_input().strip())

for i in range(1, T+1):
    n = int(raw_input().strip())
    result = count_sheep(n)
    print 'Case #' + str(i) + ': ' + str(count_sheep(n))
    #print("Case #{}: {} ".format(i, result))
