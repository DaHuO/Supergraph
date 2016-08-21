f1 = open("input2.in",'r')

f2 = open("ouput2.in",'w')

T = int(f1.readline())

for j in xrange(T):

    arr = [0,1,2,3,4,5,6,7,8,9]
    N = int(f1.readline())
    #print "N:",N
    flag = 0
    i = 0
    while flag ==0 and N != 0:
        i += 1
        t = i*N
        #print "t:",t

        while t >0:
            dig = t%10

            try:
                arr.remove(dig)

            except ValueError:
                pass

            t = t/10

        if arr == []:
            flag = 1

        #print "arr:",arr

    if N == 0:
        f2.write("Case #"+str(j+1)+": INSOMNIA \n")

    else:
        f2.write("Case #"+str(j+1)+": "+str(i*N)+"\n")

f1.close()
f2.close()

    

