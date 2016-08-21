__author__ = 'ctewani'

T = int(raw_input())
ogT = T
while T:
    N = int(raw_input())
    digit_count = {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}
    mul = 1
    prevN = 0
    currN = N
    isInsomnia = False
    while digit_count:
        currN = N * mul
        if currN == prevN:
            isInsomnia = True
            break
        for digit in str(currN):
            digit = int(digit)
            if digit in digit_count:
                del digit_count[digit]
        mul += 1
        prevN = currN

    if isInsomnia:
        print "CASE #%s: INSOMNIA"%(str(ogT - T+1))
    else:
        print "CASE #%s: %s"%(str(ogT-T+1),str(currN))

    T -= 1