from sys import stdin as sin

t = int(sin.readline())
for i in range(1,t+1):
    n = int(sin.readline())
    if n == 0:
        print('Case #%d: INSOMNIA'%(i))
        continue
    c = [0] * 10
    j = 1
    while 0 in c:
        x = str(j*n)
        for y in x:
            c[ord(y)-ord('0')] += 1
        j += 1
    print('Case #%d: %d'%(i,(j-1)*n))
