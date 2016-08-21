import copy
t=int(raw_input())
jj=1
while t>0:
    s=list((raw_input()))
    r=0
    while 1:
        #print(s)
        if s[0]=="+":
            i=0
            while i<len(s) and s[i]=="+" :
                i+=1
            if i==len(s):
                break
            else:
                for i in range(i):
                    s[i]="-"
                r+=1
        else:
            j=s[::-1].index("-")
            j=len(s)-j
            p=s[:j]
            for i in range(len(p)):
                if p[i]=="+":
                    s[j-i-1]="-"
                else:
                    s[j-i-1]="+"
            r+=1        
    print("Case #"+str(jj)+": "+str(r))
    jj+=1
    t-=1
