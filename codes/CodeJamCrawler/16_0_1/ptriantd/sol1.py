f=open('A-large.in')
g=open('Result.in','w')
T=int(f.readline())

for i in range(T):
    s=f.readline().strip()
    ww=s[0]
    for letter in s[1:]:
        if letter>=ww[0]:
            ww=letter+ww
        else:
            ww=ww+letter
            
    
    
    g.write('Case #'+str(i+1)+': '+ww+'\n')
    
    
g.close()
f.close()
