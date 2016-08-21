test=input()



for i in xrange(test):

    n=raw_input()

    ll=[n[0]]

    for j in n[1:]:
        if j >=ll[0]:
            ll.insert(0,j)
        else:
            ll.append(j)

    
            
    

        
    

    print "Case #%d: %s"%(i+1,''.join(ll))
    
    
