n=input()
ans=''
for p in range(1,n+1):
    t=raw_input()
    d=0
    l=list(t)
    while '-' in l:
        i=0
        o=l[0]
        while l[i]==o:
            i+=1
            if i>len(l)-2:
                break
        a=l[:i]
        b=l[i+1:]
        a=a[::-1]
        for q in range(len(a)):
            if a[q]=='-':
                a[q]='+'
            else:
                a[q]='-'
        l=a+b
        d+=1
    ans+='Case #'+str(p)+': '+str(d)+'\n'
print ans

        
