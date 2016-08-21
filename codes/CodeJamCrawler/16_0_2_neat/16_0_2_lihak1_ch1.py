

def f(asl):
    count = 0
    

    while asl:
        chk = len(asl) * ['+']
        chk1 = len(asl) * ['-']
        if len(asl) == 0:
            return count
        if asl == chk:
            return count
        if asl == chk1:
            count += 1
            return count
        min_ind = 0
        for i in range(len(asl)-1,-1,-1):
            
            if asl[i] == '-':
                min_ind = i
                break
                
    
        
        asl = asl[0:min_ind]
        count += 1
    
        
        for i in range(len(asl)):
            if asl[i] == '+':
                asl[i] = '-'
            else:
                asl[i] = '+'

    return count

    
    
    
    


            
        
            


            
        
            



t= int(raw_input())
for i in range(t):
   print "Case #"+str(i+1)+": "+str(f(list(raw_input())))
            
        
            


            
        
            

