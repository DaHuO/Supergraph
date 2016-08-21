import sys

def solve(initial):
    initial = int(initial)
    factor = 1
    if initial == 0:
        return "INSOMNIA"
    else:
        digits = set()
        while True:
            next_num = initial * factor
            factor += 1
            next_num = str(next_num)
            digits.update(list(next_num))
            if len(digits) == 10:
                return next_num

check = True
number_of_test_cases = 0
i = 1

for line in sys.stdin:
    if check:
        number_of_test_cases = line.strip()
        check = False
        continue
    initial = line.strip()
    got = solve(initial)
    print "Case #{0}: {1}".format(i, got)
    i += 1
