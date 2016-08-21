f = open('RankandFilein.txt','r')
g = open('RankandFileout.txt','w').close()
g = open('RankandFileout.txt','a')
t = int(f.readline())

for i in xrange(1, t+1):
    N = int(f.readline())
    n =i
    solutions = []
    myArray = []
    for i in range(0,2*N-1):
        currentLine = f.readline()
        ints = currentLine.split()
        ints = map(int,ints)
        for item in ints:
            myArray.append(item)
    for xitem in myArray:
        if ((myArray.count(xitem))%2==1):
            solutions.append(xitem)
    solutions = list(set(solutions))
    solutions.sort()
    g.write( "Case #{}:".format(n))
    for item in solutions:
        g.write(" {}".format(item))
    g.write( "\n")
g.close()
f.close()