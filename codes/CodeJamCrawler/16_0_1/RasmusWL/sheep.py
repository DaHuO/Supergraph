#!/usr/bin/env python2

f = open('A-large.in')

testcases = int(f.readline().strip())

for testcase in xrange(testcases):
    n = int(f.readline().strip())


    result = "INSOMNIA"
    mult = 1

#    digits = set([0,1,2,3,4,5,6,7,8,9])
    digits = set()

    while True:
        if n == 0:
            break

        x = n * mult

        while x:
            digit = x % 10
            x //= 10

            digits.add(digit)

        if all(i in digits for i in xrange(0,10)):
            result = mult * n
            break

        mult += 1

    print ("Case #%s: %s" % (testcase+1, result))
