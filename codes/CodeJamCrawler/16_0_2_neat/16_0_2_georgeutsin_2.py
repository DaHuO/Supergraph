t = input()

for i in range(t):
    pstr = raw_input()
    count = 0
    prevChar = pstr[0]
 
    for c in pstr:
        if not c == prevChar:
            count += 1
            if prevChar == '-':
                prevChar = '+'
            else:
                prevChar = '-'
                
    if prevChar == '-':
        count+=1
    print "Case #" + str(i+1) + ": " + str(count)
    
    