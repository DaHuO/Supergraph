def flip(s):
    s=s[::-1]
    final=""
    for i in s:
        if i=="-":
            final+="+"
        else:
            final+="-"
    return final
def lastOccur(s):
    l=len(s)
    l-=1
    while l>=0:
        if s[l]=="-":
            return l
        l-=1
    return -1
input = open("file3.txt","r")
output = open("output3.txt","w")

T = input.readline()
T = int(T)
for i in range(T):
    s=input.readline()
    ind = lastOccur(s)
    nb=0
    while ind != -1:
        nb+=1
        st = s[0:(ind+1)]
        tmp=""
        f=ind
        while st[0]!=st[f] and f>0:
            tmp+=st[f]
            f-=1
        if tmp!="":
            stk = st[0:f+1]
            stF = flip(stk)
            s=stF+tmp
            ind = lastOccur(s)
        else:
            stF=flip(st)
            ind=lastOccur(stF)
            s = stF[0:ind+1]
    
    output.write("Case #{0}: {1}\n".format(i+1,nb))