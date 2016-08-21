fr=open("output.txt","w")
fo=open("B-large.in","r")
t=int(fo.readline())
def flip(a):
    a=a[::-1]
    a=list(a)
    for i in range(len(a)):
        if a[i]=='-':
            a[i]='+'
        else:
            a[i]='-'
    return "".join(a)

t1=1
while t1<=t:
    s=fo.readline().strip()
    count=0;
    while '-' in s:
        j=len(s)
        while j>0 and s[j-1]=='+':
            j-=1
        s=s[:j]
        
        if '-' not in s:
            break
        n=0
        
        while n<len(s) and s[n]=='-':
            n+=1
        if n>0:
            s=flip(s)
            count+=1
            
            s=s[:-(n)]
        if '-' not in s:
            break   
        n=0
        
        while n<len(s) and s[n]=='+':
            n+=1
        
        s=list(s)
        s[:n]=flip(''.join(s[:n]))
        s=''.join(s)
        count+=1
        
        
    fr.write("Case #%d: %d\n" %(t1,count))
    
    t1+=1