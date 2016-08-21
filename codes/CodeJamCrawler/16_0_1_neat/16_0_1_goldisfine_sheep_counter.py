# Sam Finegold
# Google Code Challenge
# Problem 1: Sheep Counter

def unique_digits(number):
    digits = []
    while number:
        digit = number % 10
        # do whatever with digit
        digits.append(digit)
        # remove last digit from number (as integer)
        number //= 10
    return set(digits)

def multiplier(number):
    uds = {11}
    x = 11
    for i in xrange(1,100):
        uds = uds | unique_digits(x)
        uds = set(uds)
        if len(uds) > 10:
            return x
        else:
            x = i*number
    return "INSOMNIA"

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
  n = int(raw_input())
  print "Case #{}: {}".format(i, multiplier(n))
  # check out .format's specification for more formatting options
