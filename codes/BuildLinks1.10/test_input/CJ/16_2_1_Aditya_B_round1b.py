def main(x):
    x=list(x)
    li=''
    if('Z' in x):
        c=x.count('Z')
        for i in range(0,c):
            li+='0' 
            x.remove('Z')
            x.remove('E')
            x.remove('R')
            x.remove('O')
        
    
    if('W' in x):
        c=x.count('W')
        for i in range(0,c):
            li+='2' 
            x.remove('T')
            x.remove('W')
            x.remove('O')
            
        
    

    if('X' in x):
        c=x.count('X')
        for i in range(0,c):
            li+='6' 
            x.remove('S')
            x.remove('I')
            x.remove('X')
    if('G' in x):
        c=x.count('G')
        for i in range(0,c):
            li+='8' 
            x.remove('E')
            x.remove('I')
            x.remove('G')
            x.remove('H')
            x.remove('T')
            
    if('U' in x):
        c=x.count('U')
        for i in range(0,c):
            li+='4' 
            x.remove('F')
            x.remove('O')
            x.remove('U')
            x.remove('R')
      
    if('S' in x):
        c=x.count('S')
        for i in range(0,c):
            li+='7' 
            x.remove('S')
            x.remove('E')
            x.remove('V')
            x.remove('E')
            x.remove('N')
            
       
    if('V' in x):
        c=x.count('V')
        for i in range(0,c):
            li+='5' 
            x.remove('F')
            x.remove('I')
            x.remove('V')
            x.remove('E')
        
    
    if('T' in x):
        c=x.count('T')
        for i in range(0,c):
            li+='3' 
            x.remove('T')
            x.remove('H')
            x.remove('R')
            x.remove('E')
            x.remove('E')
    
    
    if('O' in x):
        c=x.count('O')
        for i in range(0,c):
            li+='1' 
            x.remove('O')
            x.remove('N')
            x.remove('E')
          
    if('N' in x):
        c=x.count('N')
        c=c/2
        for i in range(0,c):
            li+='9' 
            x.remove('N')
            x.remove('I')
            x.remove('N')
            x.remove('E')

    li=list(li)
    length=len(li)
    i=0    
    while(i<length-1):
        j=0
        while(j<length-1-i):
            if(li[j]>li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
            j+=1
        i+=1
    st=''
    for y in li:
        st+=y
                
    print st
    
    


fo = open("A-large.in", "r")

d2=fo.readlines()
for i in range(0,len(d2)):
    d2[i]=d2[i].rstrip()

t=int(d2[0])
for j in range(1,t+1):
    
    x=d2[j]
    print 'Case #'+str(j)+': ',
    main(x)
    










    
