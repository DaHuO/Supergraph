t=int(input())
for case in range(1,t+1):
    s=input()
    s1=''
    s0=s[0]
    for i in s:
        if i>=s0:
            s1=i+s1
            s0=i
        else:
            s1=s1+i
    print('Case #%s: %s'%(case,s1))
