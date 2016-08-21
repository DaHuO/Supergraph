
import math
def isprime(n, divs):
    p = 0
    N = int(math.floor(math.sqrt(n)))
    j = 2
    while j <= N:
        if n % j == 0:
            p = j
            if j not in divs:
                return j
        j +=1
    return p

finam = 'in3.txt'
fonam = 'out3.txt'
fi = open(finam)
fo = open(fonam, 'w')
T = int(fi.readline())
for t in range(T):
    cases = fi.readline().strip().split(' ')
    N = int(cases[0])
    J = int(cases[1])
    fo.write('Case #'+str(t+1)+':\n')
    M = (N-2)**2
    n = 0
    cnt = 0
    while n < M:
        s0 = bin(n)[2:]
        s = '1' + '0'*(N-2-len(s0)) + s0 + '1'
        vals = []
        nums = []
        divs = []
        for r in range(2,11):
            num = 0
            for m in range(len(s)):
                c = s[m]
                num = num * r + int(c)
            #print '-',n, num
            res = isprime(num, divs)
            if res == 0: break
            vals.append(str(res))
            nums.append(num)
            divs.append(res)
        if len(vals) >= 9:
            fo.write(s+' '+' '.join(vals)+'\n')
            print s, nums
            cnt +=1
        if cnt >= J:
            break
        n += 1

fi.close()
fo.close()
