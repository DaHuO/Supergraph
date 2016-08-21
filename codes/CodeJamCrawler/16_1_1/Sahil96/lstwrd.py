import fileinput
f=fileinput.input()

t=int(f.readline())
a=t+1
while(t>0):
    s=str(f.readline())
    i=1
    sn=[]
    sn.append(s[0])
    while(i<len(s)):
        if(s[i]<sn[0]):
            sn.append(s[i])
        else:
            sn.insert(0,s[i])
        i+=1
    sn="".join(sn)
    print "Case #{}: ".format(a-t)+sn
    t-=1
