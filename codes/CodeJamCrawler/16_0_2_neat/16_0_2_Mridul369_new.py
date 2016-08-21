fin=open('B-large.in', 'r')
fout=open('out_small.out', 'w')
t=int(fin.readline())
for x in range(t):
    s=list(fin.readline())
    a=[s[0]]
    temp=s[0]
    for i in range(1,len(s)):
        if temp!=s[i]:
            a.append(s[i])
            temp=s[i]
    if a[0]=='+':
        ans=2*(a.count('-'))
    else:
        ans=1+2*(a.count('-')-1)
    fout.write('Case #%d: '%(x+1))
    fout.write(str(ans)+'\n')
fin.close()
fout.close()
    
    
