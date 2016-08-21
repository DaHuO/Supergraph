import sys

def print_result(numCase, result):
    print "Case #"+str(numCase)+":",result

#Read file pass by argument
lines = [line.rstrip('\n') for line in open(sys.argv[1])]

T = int(lines[0])

for numCase in range(1, T+1):
    digits = [i for i in str(lines[numCase])]
    flips=0
    state = digits[0]
    for i in range(1, len(digits)):
        if (digits[i]!=state):
            state = digits[i]
            flips+=1

    if (digits[len(digits)-1] == '-'):
        flips+=1

    print_result(numCase, flips)