def dig(N, digits, result):
    
    dig1=digits[:]
    ctr=0
    T=str(N*result)
    for x in xrange(len(digits)):
        if digits[x] in T:
            del dig1[x-ctr]
            ctr+=1
    if len(dig1)==0:
        return result        
    return dig(N, dig1, result+1)

L=map(int, raw_input().split())
for x in xrange(L[0]):
    
    digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    N=L[x+1]
    result=1
    if N==0:
        print 'Case '+'#'+str(x+1)+': '+'INSOMNIA'
    else:
        print 'Case '+'#'+str(x+1)+': '+str(N*dig(N, digits, result)) 
        
    
