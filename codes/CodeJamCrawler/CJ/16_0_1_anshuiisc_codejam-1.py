fo = open("in1", "r+")

NoOftest=int(fo.readline())
# print NoOftest
j=1
while(j<NoOftest+1):
    N=int(fo.readline())
    # print N


    i=1
    # tot=list (str(N))
    tot=[]
    flag=0
    while(i<500):
        tot.append(list(str(N*i)))
        size=len(set(reduce(lambda x, y: x + y, tot)))
        # print i,set(reduce(lambda x, y: x + y, tot))
        if(size==10):
            # print N*i
            print "Case #" + str(j) + ":"  +" "+str(N*i)
            flag=1
            break
        i += 1
    if(flag==0):
        print "Case #"+str(j)+":" " INSOMNIA"
        # print "INSOMNIA"
    j+=1

