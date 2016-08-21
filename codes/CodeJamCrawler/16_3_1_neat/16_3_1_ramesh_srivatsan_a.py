
def sum(a,b):
    return a+b

def printi(i, s):
    print('Case #'+str(i)+': '+s)

t = int(raw_input())

for i in xrange(t):
    n = int(raw_input())
    a = map(int, raw_input().split())
    l = [p for p in range(n)]
    q = zip(a,l)
    q = sorted(q, key=lambda x: x[0])
    q = q[::-1]
    q = map(list, q)
    sol=''
    while reduce(sum, [a[0] for a in q])!=n:
        k=0
        while k<n-1:
            if q[k][0]!=q[k+1][0]:
                break
            k+=1
        k+=1
        if k>=3 or k==1:
            for pp in range(k):
                sol = sol + chr(q[pp][1]+ord('A'))+' '
                q[pp][0]-=1
        else:
            sol = sol + chr(q[0][1]+ord('A'))+ chr(q[1][1]+ord('A'))+' '
            q[0][0]-=1
            q[1][0]-=1
    if n-2==0:
        sol+=chr(n-2+ord('A'))+chr(n-1+ord('A'))
    else:
        sol = sol+(' '.join([chr(qq+ord('A')) for qq in range(n-2)]))+' '+chr(n-2+ord('A'))+chr(n-1+ord('A'))
    printi(i+1, sol)