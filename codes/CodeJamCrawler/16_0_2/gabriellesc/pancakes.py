import sys

transtbl = str.maketrans('+-', '-+')

def flip(stack):
    return stack.translate(transtbl)[::-1]

FIN = sys.argv[1]
fd = open(FIN, 'r')

ncases = int(fd.readline()[:-1])

for case in range(1, ncases+1):
    stack = fd.readline()[:-1]

    nflip = 0
    while '-' in stack:
        if stack[0] == '-':
            bottom = stack.rfind('-')
        else:
            bottom = stack.find('-') - 1

        stack = flip(stack[:bottom+1]) + stack[bottom+1:]

        nflip += 1
        
    print("Case #" + str(case) + ":", nflip)

