t = int(input())
print('Case #1:')
n,j = map(int,input().split())
c = 0
for i in range(0,1<<(n-2)):
    i = i*2 + 1
    i += 1<<(n-1)
    A=[]
    ok = True
    for b in range(2,11):
        k = 0
        m = 1 << (n-1)
        while m > 0:
            k *= b
            if i & m != 0:
                k += 1
            m = m >> 1
        for d in range(2,138):
            if k % d == 0:
                A.append(d)
                break
        else:
            ok = False
            break
    if ok:
        print('%s %s' %(bin(i)[2:], ' '.join(map(str,A))))
        c+=1
        if c == j:
            break
        
