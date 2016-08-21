f = open('testcase', 'r')
f1 = open('ans', 'w')
tc=int(f.readline())
#print tc
for co in range(tc):
    
    n=f.readline().rstrip('\n')
    sn=''.join(sorted(n))
    ans=sn    
    alp=[0 for i in range(26)]    
    for k in n:
        alp[ord(k)-ord('A')]+=1
    print alp
    k=[]
    if(alp[25]>0):
        t=alp[25]
        for i in range(t):            
            k.append(0)
        alp[ord('E')-ord('A')]-=alp[25]
        alp[ord('R')-ord('A')]-=alp[25]
        alp[ord('O')-ord('A')]-=alp[25]
        alp[25]=0
        print alp
    if(alp[ord('W')-ord('A')]>0):
        t=alp[ord('W')-ord('A')]
        for i in range(t):            
            k.append(2)
        alp[ord('T')-ord('A')]-=alp[ord('W')-ord('A')]
        alp[ord('O')-ord('A')]-=alp[ord('W')-ord('A')]
        alp[ord('W')-ord('A')]=0
        print alp
    if(alp[ord('U')-ord('A')]>0):
        t=alp[ord('U')-ord('A')]
        for i in range(t):            
            k.append(4)
        alp[ord('F')-ord('A')]-=alp[ord('U')-ord('A')]
        alp[ord('O')-ord('A')]-=alp[ord('U')-ord('A')]
        alp[ord('R')-ord('A')]-=alp[ord('U')-ord('A')]
        alp[ord('U')-ord('A')]=0
       
    if(alp[ord('X')-ord('A')]>0):
        t=alp[ord('X')-ord('A')]
        for i in range(t):            
            k.append(6)
        alp[ord('S')-ord('A')]-=alp[ord('X')-ord('A')]
        alp[ord('I')-ord('A')]-=alp[ord('X')-ord('A')]       
        alp[ord('X')-ord('A')]=0  
    if(alp[ord('G')-ord('A')]>0):
        t=alp[ord('G')-ord('A')]
        for i in range(t):            
            k.append(8)
        alp[ord('E')-ord('A')]-=alp[ord('G')-ord('A')]
        alp[ord('I')-ord('A')]-=alp[ord('G')-ord('A')]
        alp[ord('H')-ord('A')]-=alp[ord('G')-ord('A')]
        alp[ord('T')-ord('A')]-=alp[ord('G')-ord('A')]
        alp[ord('G')-ord('A')]=0
    if(alp[ord('O')-ord('A')]>0):
        t=alp[ord('O')-ord('A')]
        for i in range(t):            
            k.append(1)
        alp[ord('N')-ord('A')]-=alp[ord('O')-ord('A')]
        alp[ord('E')-ord('A')]-=alp[ord('O')-ord('A')]       
        alp[ord('O')-ord('A')]=0  
    if(alp[ord('T')-ord('A')]>0):
        t=alp[ord('T')-ord('A')]
        for i in range(t):            
            k.append(3)
        alp[ord('H')-ord('A')]-=alp[ord('T')-ord('A')]
        alp[ord('E')-ord('A')]-=(2*alp[ord('T')-ord('A')]) 
        alp[ord('R')-ord('A')]-=alp[ord('T')-ord('A')]    
        alp[ord('T')-ord('A')]=0  
    if(alp[ord('F')-ord('A')]>0):
        t=alp[ord('F')-ord('A')]
        for i in range(t):            
            k.append(5)
        alp[ord('I')-ord('A')]-=alp[ord('F')-ord('A')]
        alp[ord('V')-ord('A')]-=alp[ord('F')-ord('A')]     
        alp[ord('E')-ord('A')]-=alp[ord('F')-ord('A')]   
        alp[ord('F')-ord('A')]=0  
    if(alp[ord('I')-ord('A')]>0):
        t=alp[ord('I')-ord('A')]
        for i in range(t):            
            k.append(9)
        alp[ord('N')-ord('A')]-=(2*alp[ord('I')-ord('A')])
        alp[ord('E')-ord('A')]-=alp[ord('I')-ord('A')]       
        alp[ord('I')-ord('A')]=0  
    for i in range(alp[ord('S')-ord('A')]):            
        k.append(7)
    k.sort()
    ans=''.join(str(e) for e in k)
    '''
        
            
    '''    
    
    
    
    
    
    
    
    f1.write('Case #'+str(co+1)+': '+ans+'\n')