t= int(input())
for t in range(t):
    print('Case #',end='')
    print(t+1,end=': ')
    s=input()
    a=[]
    b=[s[0]]
    for i in range(len(s)):

        if s[i]>=b[0]:
            a.reverse()
            b.reverse()
            a.append(s[i])
            b.append(s[i])
            a.reverse()
            b.reverse()
        else:
            a.append(s[i])
            b.append(s[i])
    s=''.join(a)
    print(s)


