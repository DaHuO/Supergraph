from sys import stdin as ip
f=open('op.txt',"w")
for _ in xrange(int(ip.readline())):
    s=raw_input()
    flag='m'
    ct=0
    for i in s[::-1]:
        if flag=='m' and i=='-':
            ct+=1
            flag='p'
        elif flag=='p' and i=='+':
            ct+=1
            flag='m'
    f.write("Case #%d: %d\n"%(_+1,ct))
f.close()
