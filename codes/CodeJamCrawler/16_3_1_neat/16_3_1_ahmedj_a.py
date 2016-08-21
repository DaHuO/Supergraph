import sys
#f=open('test.in')
#sys.stdin = f

def choose_senats(senats):
    senats.sort(cmp=lambda a,b:b[1]-a[1])
    senats[0][1] -=1
    first= senats[0][0]
    senats.sort(cmp=lambda a,b:b[1]-a[1])
    s0 = senats[0][1]-1
    all_count = sum([senats[i][1] for i in xrange(len(senats))]) - senats[1][1] -1
    if len(senats) == 1 or senats[1][1] > 2*all_count:
        return (first,None)

    second = senats[0][0]
    senats[0][1] -=1
    return (first,second)

T = int(raw_input())
for t in xrange(T):
    N = int(raw_input())
    counts = raw_input().split(" ")
    b= ord('A')
    sol=[]
    senats = [[chr(b+i), int(counts[i])] for i in xrange(N)]
    while len(senats) > 0:
        a,b = choose_senats(senats)
        sol.append(a+b if b is not None else a)
        i=0;
        while i < len(senats):
            if senats[i][1] == 0:
                senats.pop(i)
            else:
                i+=1

    print("Case #%d: %s"%(t+1," ".join(sol)))




