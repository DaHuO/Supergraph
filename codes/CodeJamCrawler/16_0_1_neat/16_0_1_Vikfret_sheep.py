import sys

def slept(mask):
    for i in range(10):
        if not (mask & 1<<i):
            return False
    return True

T = int(raw_input())
case = 1
for x in sys.stdin:
    N = int(x)
    if N == 0:
        print "Case #"+str(case)+": INSOMNIA"
        case += 1
        continue
    i = 1
    mask = 0
    while(not slept(mask)):
        S = str(N*i)
        for idx in range(len(S)):
            mask = mask | 1<<int(S[idx])
        i += 1
    print "Case #"+str(case)+": "+str(N*(i-1))
    case += 1
