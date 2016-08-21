def order(s):
    ans=0
    for i in range(len(s)):
        ans+=(ord(s[i])-64)*28**(len(s)-i-1)
    return(ans)

file=open("A-small-attempt1.in")
k=file.readline()
a=int(k[:-1])
w=open("output.txt","w")
for num in range(a):
    k=file.readline()[:-1]
    lst={"":1}
    lst1={}
    for i in k:
        for ss in lst:
            if i+ss not in lst1:
                lst1[i+ss]=1
            if ss+i not in lst1:
                lst1[ss+i]=1
        lst.clear()
        lst=dict(lst1)
        lst1.clear()
    ans=""
    ansord=0
    for i in lst:
        if order(i)>ansord:
            ans=i
            ansord=order(i)
    s="case #"+str(num+1)+": "+ans+"\n"
    w.write(s)
w.close()
