testcases = int(raw_input())
for i in range(testcases):
    n = int(raw_input())
    c=0#just count type to increase multiplication with number
    if n==0:
        #print "Insomnia"
        print "Case #%d: Insomnia" % (i + 1)
    else:
        currvalue = n
        l = set()        
        while(len(l))<10:
            currvalue = str(n*(c+1))
            #print currvalue
            for j in currvalue:
                l.add(j)
            #print l
            c+=1
        print "Case #%d: %s" % (i + 1, c*n)