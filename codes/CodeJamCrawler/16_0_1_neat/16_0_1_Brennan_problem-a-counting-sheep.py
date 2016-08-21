
def solve(in_number):
    if in_number == 0:
        return "INSOMNIA"

    unique_digits = set()
    x, current = 1, 0
    while len(unique_digits) < 10:
        current = x * in_number
        unique_digits.update(str(current))
        x += 1
    return current

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    _raw_input = raw_input()
    number = int(_raw_input)
    solved = solve(number)
    print "Case #{}: {}".format(i, solved)
