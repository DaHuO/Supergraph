import sys

inf = sys.argv[1]

f = open(inf, 'rU')
outf = open(inf + ".out", 'w')

T = int(f.readline())
for t in xrange(T):
    stack = [True if x == '+' else False for x in f.readline().strip()]
    flips = 0
    ind = len(stack) - 1
    while ind >= 0:
        if stack[ind] == True:
            ind -= 1
            continue


        if stack[0] == True:
            for j in xrange(ind, -1, -1):
                if stack[j] == True:
                    stack[0:j+1] = [not x for x in reversed(stack[0:j+1])]
                    break
        else:
            stack[0:ind+1] = [not x for x in reversed(stack[0:ind+1])]
        flips += 1

    outf.write("Case #{0}: {1}\n".format(t+1, flips))


f.close()
outf.close()
