def getDigits(S, dig):
    ctr=True
    result=[]
    flag=True
    while flag:
        ctr=False
        if 'Z' in S:
            for x in dig[0]:
                S.remove(x)
            result.append(0)
            ctr=True
        
            
        if 'W' in S:
            for x in dig[2]:
                S.remove(x)
            result.append(2)
            ctr=True
        
        if 'U' in S:
            for x in dig[4]:
                S.remove(x)
            result.append(4)
            ctr=True
            
        if 'X' in S:
            for x in dig[6]:
                S.remove(x)
            result.append(6)
            ctr=True  
        
        if 'G' in S:
            for x in dig[8]:
                S.remove(x)
            result.append(8)
            ctr=True
        
        flag=ctr
        
    flag=True
    
    while flag:
        ctr=False
        
        if 'O' in S:
            for x in dig[1]:
                S.remove(x)
            result.append(1)
            ctr=True
            
        if 'H' in S:
            for x in dig[3]:
                S.remove(x)
            result.append(3)
            ctr=True 
            
        if 'F' in S:
            for x in dig[5]:
                S.remove(x)
            result.append(5)
            ctr=True
            
        flag=ctr
        
    flag=True
    while flag:
        ctr=False
        
        if 'S' in S:
            for x in dig[7]:
                S.remove(x)
            result.append(7)
            ctr=True
            
        if 'N' in S:
            for x in dig[9]:
                S.remove(x)
            result.append(9)
            ctr=True   
        
        flag=ctr
    
    result.sort()
    res=""
    for x in result:
        res+=str(x)
    return res
        
dig={0:"ZERO", 1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR", 5:"FIVE", 6:"SIX", 7:"SEVEN", 8:"EIGHT", 9:"NINE"}
L=map(str, raw_input().split())

for x in xrange(1, int(L[0])+1):
    S=[]
    map(S.extend, L[x])
    res=getDigits(S, dig)
    print "Case #"+str(x)+": "+res