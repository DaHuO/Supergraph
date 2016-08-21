def isInsomnia(input):
    if input == (input * 3):
        return True
    return False

input = int(raw_input())
check = [0] * 10
multiplier = 1

for x in xrange(input):
    currentInput = int(raw_input())
    
    if isInsomnia(currentInput) == False:
        while True:
            num = currentInput * multiplier
            sNum = str(num)
            for digit in sNum:
                check[int(digit)] = 1
            if sum(check) == 10:
                print "Case #" + str(x+1) + ": " + str(num)
                break
            multiplier += 1
    else:
        print "Case #" + str(x+1) + ": INSOMNIA"
    multiplier = 1
    check = [0] * 10
