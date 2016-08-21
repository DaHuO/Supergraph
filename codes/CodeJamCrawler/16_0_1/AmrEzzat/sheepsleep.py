dataInput=open('C:\Users\AmrEzzat\Desktop\A-large.in')
dataOutput=open('C:\Users\AmrEzzat\Desktop\A-large.out','wb')
t = int(dataInput.readline())  # read a line with a single integer
for i in xrange(1, t + 1):
    #n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    #print "Case #{}: {} {}".format(i, n + m, n * m)
    # check out .format's specification for more formatting options
    remaining=[0,1,2,3,4,5,6,7,8,9]
    N=int(dataInput.readline())
    counter=2
    while(len(remaining)>0):
        currentN=N
        while(currentN>0):        
            currentNumber=currentN%10
            currentN=currentN/10
            if currentNumber in remaining:
                remaining.remove(currentNumber)
        N=N*counter/(counter-1)
        counter+=1
        if counter>100: break
    if len(remaining)==0:
        dataOutput.write("Case #{}: {}".format(i, N-N/(counter-1))+"\n")
        print "Case #{}: {}".format(i, N-N/(counter-1))
    else:
        dataOutput.write("Case #{}: {}".format(i,"INSOMNIA")+"\n")
        print "Case #{}: {}".format(i,"INSOMNIA")
dataInput.close()
dataOutput.close()