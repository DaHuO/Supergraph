
m = int(input())
for l in range(1,m+1):
    k,c,s = input().split()
    k = int(k)
    c = int(c)
    s = int(s)
    print("Case #",l,": ", sep='', end='')
    k2 = k**(c-1)
    for i in range(s):
        print(1+i*k2,' ', sep='', end='')
    print()
