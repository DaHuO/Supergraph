fin=open('A-large.in', 'r')
fout=open('small.out', 'w')
t=int(fin.readline())
for x in range(t):
    s=fin.readline()
    a=[s[0]]
    for i in range(1, len(s)):
        if ord(s[i])>=ord(a[0]):
            a.insert(0, s[i])
        else:
            a.append(s[i])
    a=''.join(a)
    fout.write('Case #%d: '%(x+1)+a+'\n')
            
fin.close()
fout.close()
    
    
