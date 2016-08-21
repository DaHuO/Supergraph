def fun(s,i):
    return 2*s[i:].count("+-")
tc=int(raw_input())
for case in range(1,tc+1):
    inp=raw_input()
    l=len(inp)
    ans=0
    i=0
    if inp[0]=="-":
        ans=1
        i=1
        while i<l:
            if inp[i]=="+":
                break
            i=i+1
    ans=ans+fun(inp,i)
    print "Case #"+str(case)+": "+str(ans)
        
            
            
