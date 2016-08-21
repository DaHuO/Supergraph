


outfile=open('outfileLA_SO2016','w')

with open("A-large.in") as fil:
    cases=int(fil.readline())
    out=""
    for case in xrange(cases):
        testline=fil.readline().split()
        N=int(testline[0]); i=2;
        result=N
        list_nbr=str(N)
        while len(set(list_nbr))<10 and N!=0:
            result=N*i
            list_nbr=list_nbr+str(result)
            i+=1
        if N==0:
            result="INSOMNIA"
        out+=("Case #%d: %s\n")%( case+1, result)
        
    
#print out
outfile.write(out)
outfile.close()
