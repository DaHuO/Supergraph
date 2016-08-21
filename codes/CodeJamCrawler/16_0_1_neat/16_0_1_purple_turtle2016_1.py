def count_digit(n):
    if n==0:
        return 0
    s=set()
    c=1
    while True:
        m=n*c
        for i in str(m):
            s.update(i)
        print s
        if len(s)==10:
            break
        c+=1

    return m

f=open("A-large.in","r")
t=int(f.readline().strip("\n"))
f2=open("A-large.out","w")
for i in range(1,1+t):
    n=int(f.readline().strip("\n"))

    c=count_digit(n)
    if c==0:
        c="INSOMNIA"
    f2.write("Case #"+str(i)+": "+str(c)+"\n")
f.close()
f2.close()


