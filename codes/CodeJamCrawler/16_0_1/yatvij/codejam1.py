f = open('codejam1in.txt','r')

t = int(f.readline())  # read a line with a single integer

for i in xrange(1, t+1):
    n = int(f.readline()) 
    iterator = 1
    mymax = 0
    myArray = ['0','1','2','3','4','5','6','7','8','9']
    while (myArray != []):
        if(n==0):
            mymax = "INSOMNIA"
            break
        for digit in str(iterator*n):
            if digit in myArray:
                myArray.remove(digit)
                mymax = iterator*n
        iterator+=1
    g = open('codejam1out.txt','a')
    g.write( "Case #{}: {}\n".format(i, mymax))
    g.close()
f.close()
    # check out .format's specification for more formatting options