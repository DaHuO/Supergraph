#!/usr/bin/env python

cases = raw_input()
cases = int(cases)

for case in range(1, cases + 1):
    number = raw_input()
    number = int(number)

    current = number
    digits = []
    while True:
        for c in str(current):
            if c not in digits:
                digits.append(c)
        if len(digits) >= 10:
            break
        current += number
        if current == number:
            break

    if len(digits) < 10:
        output = 'Case #%d: INSOMNIA' % case
    else:
        output = 'Case #%d: %d' % (case, current)
    print(output)
