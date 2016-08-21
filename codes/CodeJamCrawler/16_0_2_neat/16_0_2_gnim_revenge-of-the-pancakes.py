import sys
import fileinput

def answer(cookie):
    total = 0
    idx = 0
    for i in range(0, len(cookie)-1):
        if  cookie[i] == '+' and cookie[i+1] == '-':
            total += 2
        i += 1
    if cookie[0] == '-':
        return  total + 1
    else:
        return total



inputs  = [line.rstrip() for line in fileinput.input()]
for num in range(1, int(inputs[0])+1):
    print "Case #" + str(num) + ": " +  str(answer(inputs[num]))
