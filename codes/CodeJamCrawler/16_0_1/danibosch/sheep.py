import sys

t = int(raw_input())
for i in xrange(1, t + 1):
    number = int(raw_input())
    if number == 0:
        print "Case #{}: INSOMNIA".format(i)
    else:
        digits = []
        j = 1
        n = number
        while len(digits) != 10 and j < 100000000:
            n = number * j
            digitnumber = n
            
            while digitnumber >= 10:
                digit = digitnumber % 10
                digitnumber /= 10
                if digit not in digits:
                    digits.append(digit)
                    
            digit = digitnumber
            if digit not in digits:
                digits.append(digit)
            j += 1
        if j >= 100000000:
            print "Case #{}: INSOMNIA".format(i)
        else:
            print "Case #{}: {}".format(i, n)
        