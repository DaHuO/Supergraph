t = input()

i = 1
while t:
    t -= 1
    s = list(raw_input().strip())
    if '+' not in s:
        print "Case #" + str(i) + ": 1"
    elif '-' not in s:
        print "Case #" + str(i) + ": 0"
    else:
        plusEncourted = 0
        negativeEnded = 1
        count = 0
        for each in s:
            if each == '+':
                plusEncourted = 1
                negativeEnded = 1
            elif each == '-':
                if negativeEnded:
                    if plusEncourted:
                        count += 1
                    count += 1
                    negativeEnded = 0
        print "Case #" + str(i) + ": " + str(count)
    i += 1