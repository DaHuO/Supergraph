        #Contestant : Emmanuel HAVUGIMANA
        #Year 2016
        #Country Rwanda
t = int(input())
caseN=0

for i in xrange(1,t+1):
    n=int([int(s) for s in raw_input().split()][0])
    l=set()
    nNext=0
    
    if n==0:   # for infititely long time before getting all digits, I assumed that it true only for 0
        caseN+=1
        print "Case #{}: {}".format(str(caseN),"INSOMNIA")
    else:   # for other cases,I used sets to store elements until it gets 10 elements
        caseN+=1
        while len(l)!=10:
            nNext+= n
            for s in str(nNext):
                l.add(s)
        print "Case #{}: {}".format(str(caseN),str(nNext))



    
##n2=0
##l=set()
##caseN=0
##if n==0:
##    caseN+=1
##    print "Case #{}: {}".format(str(caseN),"Insomia")
##    
##else:
##    caseN+=1
##    while len(l)!=10:
##        n2+= n
##        for s in str(n2):
##            l.add(s)
##    print "Case #{}: {}".format(str(caseN),str(n2))
##
