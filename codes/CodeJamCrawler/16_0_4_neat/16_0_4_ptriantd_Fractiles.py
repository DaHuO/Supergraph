f=open('D-small-attempt2.in')
g=open('Result.in','w')
T=int(f.readline())

for i in range(T):
    
    K,C,S = map(int,f.readline().split())
    
    g.write('Case #'+str(i+1)+': ')
    for j in range(1,K):
        g.write(str(j)+' ')
    g.write(str(K)+'\n')
    
        
    
    
g.close()
f.close()
