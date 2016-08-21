def problem_a():

    t =  int(raw_input()) #number of test cases
    for i in xrange(1,t+1):
        n = int(raw_input())
        n1 = n
        d ={}
        for z in range(0,10):
            d ={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
        if n==0:
            n = "INSOMNIA"
        else:
            m = 2
            while(len([y for y in d.keys() if d[y]>0])!=10):
                for ch in str(n):
                    d[ch]+=1
                if(len([y for y in d.keys() if d[y]>0])==10):
                    break
                n = n1*m
                m+=1
        print "Case #{}: {}".format(i, n)
            
            
                
                
        
        



problem_a()
