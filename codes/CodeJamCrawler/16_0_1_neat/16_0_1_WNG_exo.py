def nbsleep(N):
    if N==0:
        return "INSOMNIA"
    else:
        hasseen=[False]*10
        nb=0
        currN=0
        while not all(hasseen):
            currN+=N
            nb+=1
            tN=currN
            while tN>0:
                digit=tN%10
               # print tN
                #print digit
                hasseen[digit]=True
                tN=tN/10
            if nb%10000==0:
                print "ca fait bcp non?"
                return 0
        return currN
    
contenu=[int(line.rstrip('\n')) for line in open("A-large.in")]
nbl=contenu[0]
print nbl
with open("output_large.txt","w+") as f:
    for i in range(1,nbl+1):
        start=contenu[i]
        res=nbsleep(start)
        print "{} {}".format(start,res)
        f.write("Case #{}: {}\n".format(i,res))


    


