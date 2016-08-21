from sys import stdin
from sys import stdout
flag = [False] * 10
def isDone(n):
    for k in str(n):
        flag[int(k)] = True
    if False in flag:
        return True
    return False
def cleanFlag():
    for i in range(10):
        flag[i] = False


t = stdin.readline()
for i in range(int(t)):
    n = int(stdin.readline())
    j = 1
    p = n * j
    if n != 0:
        while isDone(p):
            j += 1
            p = n * j
        print "Case #" + str(i + 1) + ": " + str(p)
        cleanFlag()
    else:
        print "Case #" + str(i + 1) + ": INSOMNIA"
