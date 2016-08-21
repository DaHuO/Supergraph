
def ch(s):
    i = 1
    final = s[0]
    
    while i < len(s):
        curr = s[i]
        
        cmp1 = final[0]
        if curr >= cmp1:
            final = curr+final
        else:
            final = final + curr
        i += 1
        
    return final

            
        
            


            
        

t= int(raw_input())
for i in range(t):
     
   print "Case #"+str(i+1)+": "+str(ch(str(raw_input())))
            
        
            


            
        
            

