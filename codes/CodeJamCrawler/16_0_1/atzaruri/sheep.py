import sys

T = int(sys.stdin.readline())

def split(number, digits):
    while number > 0:
        digits[number % 10] = True
        number /= 10

for test in xrange(T):
    n = int(sys.stdin.readline())

    if n != 0:
        digits = [False] * 10
        done = False
        multiplier = 0

        while not done:
            multiplier += 1

            split(multiplier * n, digits)

            done = True
            for b in digits:
                done = done and b

    print "Case #" + str(test + 1) + ":",
    if n != 0:
         print multiplier * n
    else:
        print "INSOMNIA"
