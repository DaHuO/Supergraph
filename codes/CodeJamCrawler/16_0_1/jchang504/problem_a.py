import sys

# Removes from digits any digits present in ni
def find_digits(digits, ni):
    while ni > 0:
        d = ni % 10
        for target in digits:
            if d == target:
                digits.remove(target)
        ni /= 10

# If Bleatrix counts by n starting from n, return the last number she will
# count to before she sees all the digits 0-9
def bleatrix(n):
    if n == 0:
        return 0
    else:
        ni = 0
        digits_missing = [i for i in xrange(10)]
        while len(digits_missing) > 0:
            ni += n
            find_digits(digits_missing, ni)
        return ni

input_lines = sys.stdin.readlines()
num_cases = int(input_lines[0])

for i in xrange(1, num_cases+1):
    n = int(input_lines[i])
    answer = bleatrix(n)
    print "Case #%d: %s" % (i, "INSOMNIA" if answer == 0 else str(answer))
