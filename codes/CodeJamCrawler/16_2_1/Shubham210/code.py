a = int(input())
for i in range(a):

    number0=0
    number1=0
    number2=0
    number3=0
    number4=0
    number5=0
    number6=0
    number7=0
    number8=0
    number9=0

    p=""
    
    stringData = input()


    while(stringData.count('Z')>0 and stringData.count('E')>0 and stringData.count('R')>0 and stringData.count('O')>0):
        number0+=1
        stringData=stringData.replace('Z','',1)
        stringData=stringData.replace('E','',1)
        stringData=stringData.replace('R','',1)
        stringData=stringData.replace('O','',1)

    while(stringData.count('S')>0 and stringData.count('I')>0 and stringData.count('X')>0):
        number6+=1
        stringData=stringData.replace('S','',1)
        stringData=stringData.replace('I','',1)
        stringData=stringData.replace('X','',1)

    while(stringData.count('E')>0 and stringData.count('I')>0 and stringData.count('G')>0 and stringData.count('H')>0 and stringData.count('T')>0):
        number8+=1
        stringData=stringData.replace('E','',1)
        stringData=stringData.replace('I','',1)
        stringData=stringData.replace('G','',1)
        stringData=stringData.replace('H','',1)
        stringData=stringData.replace('T','',1)

    while(stringData.count('S')>0 and stringData.count('E')>1 and stringData.count('V')>0 and stringData.count('N')>0):
        number7+=1
        stringData=stringData.replace('S','',1)
        stringData=stringData.replace('E','',1)
        stringData=stringData.replace('V','',1)
        stringData=stringData.replace('E','',1)
        stringData=stringData.replace('N','',1)

    while(stringData.count('T')>0 and stringData.count('H')>0 and stringData.count('R')>0 and stringData.count('E')>1):
        number3+=1
        stringData=stringData.replace('T','',1)
        stringData=stringData.replace('H','',1)
        stringData=stringData.replace('R','',1)
        stringData=stringData.replace('E','',1)
        stringData=stringData.replace('E','',1)
    
   

    while(stringData.count('F')>0 and stringData.count('O')>0 and stringData.count('U')>0 and stringData.count('R')>0):
        number4+=1
        stringData=stringData.replace('F','',1)
        stringData=stringData.replace('O','',1)
        stringData=stringData.replace('U','',1)
        stringData=stringData.replace('R','',1)

    while(stringData.count('F')>0 and stringData.count('I')>0 and stringData.count('V')>0 and stringData.count('E')>0):
        number5+=1
        stringData=stringData.replace('F','',1)
        stringData=stringData.replace('I','',1)
        stringData=stringData.replace('V','',1)
        stringData=stringData.replace('E','',1)

    while(stringData.count('N')>1 and stringData.count('I')>0 and stringData.count('E')>0):
        number9+=1
        stringData=stringData.replace('N','',1)
        stringData=stringData.replace('I','',1)
        stringData=stringData.replace('N','',1)
        stringData=stringData.replace('E','',1)
        
    
        
    while(stringData.count('T')>0 and stringData.count('W')>0 and stringData.count('O')>0):
        number2+=1
        stringData=stringData.replace('T','',1)
        stringData=stringData.replace('W','',1)
        stringData=stringData.replace('O','',1)
        
       
    
        
    

    
    while(stringData.count('O')>0 and stringData.count('N')>0 and stringData.count('E')>0):
        number1+=1
        stringData=stringData.replace('O','',1)
        stringData=stringData.replace('N','',1)
        stringData=stringData.replace('E','',1)
    
    
    

    while(number0>0):
        p+=str(0)
        number0-=1

    while(number1>0):
        p+=str(1)
        number1-=1

    while(number2>0):
        p+=str(2)
        number2-=1

    while(number3>0):
        p+=str(3)
        number3-=1

    while(number4>0):
        p+=str(4)
        number4-=1

    while(number5>0):
        p+=str(5)
        number5-=1

    while(number6>0):
        p+=str(6)
        number6-=1

    while(number7>0):
        p+=str(7)
        number7-=1
    while(number8>0):
        p+=str(8)
        number8-=1
    while(number9>0):
        p+=str(9)
        number9-=1
        
    print("Case #"+str(i+1)+": "+p)
    p=""
    
