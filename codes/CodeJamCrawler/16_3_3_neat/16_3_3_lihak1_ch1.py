
def ch(al):
    j,p,s,k = al
    final = []
    djp = {}
    djs = {}
    dps = {}
    l = [(q,w,e) for q in range(1,j+1) for w in range(1,p+1) for e in range(1,s+1) if not q==w==e]
    
    
    
    for (a,s,d) in l:
        if (a,s) not in djp:
            djp[(a,s)] = 1
        else:
            djp[(a,s)] += 1
        if (a,d) not in djs:
            djs[(a,d)] = 1
        else:
            djs[(a,d)] += 1
        if (s,d) not in dps:
            dps[(s,d)] = 1
        else:
            dps[(s,d)] += 1
        
        if djp[(a,s)] <= k and djs[(a,d)] <= k and dps[(s,d)] <= k:
                    final.append((a,s,d))
        else:
            djp[(a,s)] -= 1
            djs[(a,d)] -= 1
            dps[(s,d)] -= 1
    l = [(q,w,e) for q in range(1,j+1) for w in range(1,p+1) for e in range(1,s+1) if  q==w==e]
    for (a,s,d) in l:
        if (a,s) not in djp:
            djp[(a,s)] = 1
        else:
            djp[(a,s)] += 1
        if (a,d) not in djs:
            djs[(a,d)] = 1
        else:
            djs[(a,d)] += 1
        if (s,d) not in dps:
            dps[(s,d)] = 1
        else:
            dps[(s,d)] += 1
        
        if djp[(a,s)] <= k and djs[(a,d)] <= k and dps[(s,d)] <= k:
                    final.append((a,s,d))

        else:
            djp[(a,s)] -= 1
            djs[(a,d)] -= 1
            dps[(s,d)] -= 1
    return final
            
            
        

        
            


            
        

t= int(raw_input())
for i in range(t):
   l = []
   l1 = map(int, raw_input().split())
   
  
   print "Case #"+str(i+1)+": "+str(len(ch(l1)))
   for ele in ch(l1):
    print ele[0],ele[1],ele[2]
            
        
            


            
        
            

