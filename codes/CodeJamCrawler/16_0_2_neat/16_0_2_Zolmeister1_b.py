# Zolmeister

import sys
from bitarray import bitarray

fout = open(sys.argv[0] + '.out', 'w')

def pp(t, s):
    out = 'Case #{}: {}'.format(t + 1, s)
    print out
    fout.write(out + '\n')



T = int(input())

for t in xrange(T):
    line = raw_input()
    flips = 0
    stack = bitarray()
    for bit in line:
        if bit == '-':
            stack.append(0)
        else:
            stack.append(1)

    # trim trues
    def trim(stack):
        cnt = 0
        for i in xrange(len(stack) - 1, -1, -1):
            if stack[i] == False:
                break
            cnt += 1
        return cnt

    # print stack

    while not stack.all():
        if stack[0] == True:
            # flip set of leading 1s
            # print 'leading'
            for i, bit in enumerate(stack):
                if bit is True:
                    stack[i] = False
                else:
                    break
            # print stack
        else:
            # print 'trim'
            cnt = trim(stack)
            if cnt > 0:
                stack = stack[:-cnt]
            # print stack

            # flip!
            # print 'flip'
            stack.reverse()
            # print stack

            # print 'invert'
            for i in xrange(len(stack)):
                stack[i] = not stack[i]

            # print stack

        flips += 1
        # if flips > 3:
        #     break

    # print 'done'
    # print 'flips', flips
    pp(t, flips)



fout.close()
