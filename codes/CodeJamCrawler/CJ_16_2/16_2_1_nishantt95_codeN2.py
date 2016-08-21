a = int(input())
for i in range(a):

    z0=0
    z1=0
    z2=0
    z3=0
    z4=0
    z5=0
    z6=0
    z7=0
    z8=0
    z9=0

    p=""
    
    s = input()


    while(s.count('Z')>0 and s.count('E')>0 and s.count('R')>0 and s.count('O')>0):
        z0+=1
        s=s.replace('Z','',1)
        s=s.replace('E','',1)
        s=s.replace('R','',1)
        s=s.replace('O','',1)

    while(s.count('S')>0 and s.count('I')>0 and s.count('X')>0):
        z6+=1
        s=s.replace('S','',1)
        s=s.replace('I','',1)
        s=s.replace('X','',1)

    while(s.count('E')>0 and s.count('I')>0 and s.count('G')>0 and s.count('H')>0 and s.count('T')>0):
        z8+=1
        s=s.replace('E','',1)
        s=s.replace('I','',1)
        s=s.replace('G','',1)
        s=s.replace('H','',1)
        s=s.replace('T','',1)

    while(s.count('S')>0 and s.count('E')>1 and s.count('V')>0 and s.count('N')>0):
        z7+=1
        s=s.replace('S','',1)
        s=s.replace('E','',1)
        s=s.replace('V','',1)
        s=s.replace('E','',1)
        s=s.replace('N','',1)

    while(s.count('T')>0 and s.count('H')>0 and s.count('R')>0 and s.count('E')>1):
        z3+=1
        s=s.replace('T','',1)
        s=s.replace('H','',1)
        s=s.replace('R','',1)
        s=s.replace('E','',1)
        s=s.replace('E','',1)
    
   

    while(s.count('F')>0 and s.count('O')>0 and s.count('U')>0 and s.count('R')>0):
        z4+=1
        s=s.replace('F','',1)
        s=s.replace('O','',1)
        s=s.replace('U','',1)
        s=s.replace('R','',1)

    while(s.count('F')>0 and s.count('I')>0 and s.count('V')>0 and s.count('E')>0):
        z5+=1
        s=s.replace('F','',1)
        s=s.replace('I','',1)
        s=s.replace('V','',1)
        s=s.replace('E','',1)

    while(s.count('N')>1 and s.count('I')>0 and s.count('E')>0):
        z9+=1
        s=s.replace('N','',1)
        s=s.replace('I','',1)
        s=s.replace('N','',1)
        s=s.replace('E','',1)
        
    
        
    while(s.count('T')>0 and s.count('W')>0 and s.count('O')>0):
        z2+=1
        s=s.replace('T','',1)
        s=s.replace('W','',1)
        s=s.replace('O','',1)
        
       
    
        
    

    
    while(s.count('O')>0 and s.count('N')>0 and s.count('E')>0):
        z1+=1
        s=s.replace('O','',1)
        s=s.replace('N','',1)
        s=s.replace('E','',1)
    
    
    

    while(z0>0):
        p+=str(0)
        z0-=1

    while(z1>0):
        p+=str(1)
        z1-=1

    while(z2>0):
        p+=str(2)
        z2-=1

    while(z3>0):
        p+=str(3)
        z3-=1

    while(z4>0):
        p+=str(4)
        z4-=1

    while(z5>0):
        p+=str(5)
        z5-=1

    while(z6>0):
        p+=str(6)
        z6-=1

    while(z7>0):
        p+=str(7)
        z7-=1
    while(z8>0):
        p+=str(8)
        z8-=1
    while(z9>0):
        p+=str(9)
        z9-=1
        
    print("Case #"+str(i+1)+": "+p)
    p=""
    
