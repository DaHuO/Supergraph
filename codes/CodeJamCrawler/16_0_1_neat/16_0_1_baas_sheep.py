import sys

l = sys.stdin.readlines()
numbers = [int(num.strip()) for num in l[1:]]

def solve(num):
    s = str()
    i = 1
    digits = dict()
    while len(digits) != 10:
        s = str(i*num)
        for c in s:
            digits[int(c)] = 1
        i += 1

    return s


for i, num in zip(range(len(numbers)), numbers):
    if 0 == num:
        print "Case #{}: {}".format(i+1, "INSOMNIA")
    else:
        print "Case #{}: {}".format(i+1, solve(num))


