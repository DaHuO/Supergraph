try:
    T=int(raw_input())
    if 1<=T<=100:
        for z in range(T):
            Integers=[]
            N=int(raw_input())
            if 0<=N<=10**6:
                i=1
                while i<1000:
                    y=i*N
                   
                    for q in list(str(y)):
                        if q not in Integers:
                            Integers.append(q)
                    if len(Integers)==10:
                        print 'Case #'+str(z+1)+':',y
                        break
                    i+=1
                else:
                    print 'Case #'+str(z+1)+':','INSOMNIA'
            else:
                print "N should be between 0 to 10**6"
    else:
        print "T should be in range of  0 to 100 "
except ValueError:
    print "Use Integers Only"
        
             
    
                
    
    
