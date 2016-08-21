import sys


fh = open("/Users/malzantot/Documents/codingspace/D-small-attempt0.in.txt", "r")
tt = int(fh.readline())

for it in range(1, tt+1):
    sys.stdout.write("Case #%d:" %it)

    k, c, s = [int(x) for x in fh.readline().split()]

    if (c==1 and s < k):
        print(" IMPOSSIBLE")
    elif(c==1 and s==k):
        for x in range(1, k+1):
            sys.stdout.write(" %d" %(x))
        print("")
    else:
        # more tricky case c > 1
        for x in (range(1, k**c+1, k**(c-1))):
            sys.stdout.write(" %d" %(x))
        print("")

