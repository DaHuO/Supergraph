def count_flip(s):
    cur=s[0]
    count=1
    for c in s:
        if c!=cur:
            count+=1
            cur=c
    if s[-1]=="+":
        count-=1
    return count

f=open("B-large.in","r")
t=int(f.readline().strip("\n"))
f2=open("B-large.out","w")
for i in range(1,1+t):
    s=f.readline().strip("\n")

    c=count_flip(s)

    f2.write("Case #"+str(i)+": "+str(c)+"\n")
f.close()
f2.close()