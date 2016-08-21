f=open('B-large.in')
g=open('Result.in','w')
T=int(f.readline())

for i in range(T):
    s=f.readline().strip()
    
    
    flips=0
    if len(s)==1:
        if s[0]=='-':
            flips=1
    else:
        for j in range(0,len(s)):
            if s[j]=='-':
                if j<len(s)-1:
                    if s[j+1]=='-':
                        continue
                    else:
                        if s[0]=='-':
                            flips+=1
                        else:
                            flips+=2
                        s = '+'*(j+1)+s[j+1:]
                else:
                    if s[0]=='-':
                        flips+=1
                    else:
                        flips+=2
    g.write('Case #'+str(i+1)+': '+str(flips)+'\n')
    
    
g.close()
f.close()
