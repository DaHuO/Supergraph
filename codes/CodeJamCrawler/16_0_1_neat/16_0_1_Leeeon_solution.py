caseCount = int(raw_input())

for caseNum in xrange(1, caseCount + 1):

    numsLeft = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number = long(raw_input())
    currentNumber = number
    i = 0

    if number == 0:
        print "Case #{}: INSOMNIA".format(caseNum)
    else:
        while len(numsLeft) > 0:
             #get digits
             digits = [ int(digit) for digit in str(currentNumber)]

             #remove digits
             for digit in digits:
                if digit in numsLeft:
                    numsLeft.remove(digit)

             #validate nums left
             if len(numsLeft) > 0:
                 i += 1
                 currentNumber = i * number
             else:
                 print "Case #{}: {}".format(caseNum, currentNumber)
                 break;
