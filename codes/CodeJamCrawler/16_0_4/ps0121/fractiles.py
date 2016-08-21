def findnum(k,pos,c):
    if c==1:
        return pos+1
    else:
        return ((k**c)/k)*pos+findnum(k,pos,c-1)

#get input
t=int(raw_input())
for i in range(1,t+1):
    tempin=raw_input()
    tempin=tempin.split(" ")
    k=int(tempin[0])
    #print k
    c=int(tempin[1])
    #print c
    s=int(tempin[2])
    #print s

    result=[0]*s
    result[0]=1
    result[s-1]=k**c

    if k>2:
        for pos in range(1,k-1):
            res=findnum(k,pos,c)
            #print res
            result[pos]=res
    
    print "Case #%d: %s" % (i,' '.join(map(str,result)))
