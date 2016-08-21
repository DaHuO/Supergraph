def checkEqual(lst):
    return not lst or lst.count(lst[0]) == len(lst)

line = raw_input()
T = int(line)
numbers = []

for e in range(0, T):
    line = raw_input()
    numbers.append(line)
    
for n in range(0, len(numbers)):
    i = 0
    found = [False]*10
    foundAll = False
    if int(numbers[n]) == 0:
        print "Case #" + str(n+1) + ": INSOMNIA"
    else:
        while not foundAll:
            actualNumber = (i+1)*int(numbers[n])
            numberList = list(str(actualNumber))
            for digit in numberList:
                if found[int(digit)] == False:
                    found[int(digit)] = True
                    if checkEqual(found):
                        foundAll = True
            i += 1
        print "Case #" + str(n+1) + ": " + str(actualNumber)