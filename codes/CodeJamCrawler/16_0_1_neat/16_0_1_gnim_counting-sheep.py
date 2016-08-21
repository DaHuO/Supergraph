import sys
import fileinput
from sets import Set

def answer(inp):
    inp = int(inp)
    if inp == 0:
        return "INSOMNIA"
    s = Set([e for e in range(0, 10)])
    multi = 0
    while s:
        multi += 1
        temp = inp * multi
        while temp:
            s.discard(temp % 10)
            temp /= 10
    return str(inp * multi)


inputs  = [line.rstrip() for line in fileinput.input()]
for num in range(1, int(inputs[0])+1):
    print "Case #" + str(num) + ": " +  str(answer(inputs[num]))
