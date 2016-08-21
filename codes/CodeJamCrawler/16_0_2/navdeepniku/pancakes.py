#f = open('A-large.in')
#fo = open('output.out','wb')
#t= int(f.readline().strip())

def changer(s):
    t=len(s)
    s=list(s)
    s.append('n')
    for i in range(0,t):
        if s[i]==s[i+1] or s[i+1]=='n':
            if s[i]=='0':
                s[i]='1'
            else:
                s[i]='0'
        else:
            if s[i]=='0':
                s[i]='1'
            else:
                s[i]='0'
            return ''.join(s[:t])
    return ''.join(s[:t])

def transform(s):
    t=''
    for i in s:
        if i=='+':
            t=t+'0'
        else:
            t=t+'1'
    return t


f = open('B-large.in')
fo = open('output.out','wb')
t= int(f.readline().strip())
for i in range(1,t+1):
    s= f.readline().strip()
    s=transform(s)
    n=0
    while(int(s)!=0):
        s=changer(s)
        
        n=n+1
    fo.write('Case #'+str(i)+': '+str(n)+'\n')
    
f.close()
fo.close()
