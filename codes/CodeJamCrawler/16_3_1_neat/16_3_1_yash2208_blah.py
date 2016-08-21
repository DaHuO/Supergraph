with open("A-large.in", 'r') as inputfile:
    with open("output.txt", 'w') as outputfile:
        for _ in xrange(int(inputfile.readline())):
            n,output=int(inputfile.readline()),""
            a=map(int, inputfile.readline().split())
            while sum(a) > 0 and (sum(a)!=3 or max(a)!=1):
                temp=a.index(max(a))
                a[temp]-=1
                temp2=a.index(max(a))
                a[temp2]-=1
                output+=chr(temp+65)+chr(temp2+65)+" "
            if sum(a) > 0:
                temp=a.index(1)
                a[temp]-=1
                output+=chr(temp+65)+" "
                temp=a.index(1)
                a[temp]-=1
                temp2=a.index(1)
                a[temp2]-=1
                output+=chr(temp+65)+chr(temp2+65)+" "
            outputfile.write("Case #" + str(_+1) + ": " + output + "\n")
