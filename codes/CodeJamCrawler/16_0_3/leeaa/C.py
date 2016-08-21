PT = [2,3,5,7]
PTs = [[],[]]

def isPrime(x, base):
    for j in PTs[base]:
        if x%j == 0:
            return j
    return 0

def int2base(x):
    ret = []
    while x:
        ret.append(x%2)
        x /= 2
    ret.reverse()
    return ''.join(map(str,ret))


M = 2**16

for i in xrange(9, M, 2):
    isP = True
    for j in PT:
        if i%j == 0:
            isP = False
            break
        if j*j>i:
            break
    if isP:
        PT.append(i)


for i in xrange(2,11):
    PTs.append([2,3,5,7])
    for p in PT:
        if (p-1)%i == 0:
            PTs[-1].append(p)

tn = int(raw_input())
for tc in xrange(1, tn+1):
    N, J = map(int, raw_input().split())
    print 'Case #' + str(tc) +':'
    now = 2**(N-1)+1
    ans = 0
    while now<2**N and ans < J:
        s = int2base(now)
        notP = True
        tmp = []
        for i in xrange(2,11):
            r = isPrime(int(s,i), i)
            if r == 0:
                notP = False
                break
            tmp.append(r)
        if notP:
            print s, ' '.join(map(str,tmp))
            ans += 1
        now += 2
#print PT[:30]
