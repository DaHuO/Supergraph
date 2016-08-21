T = int(raw_input())  # read a line with a single integer
for i in xrange(1, T + 1):
    N = raw_input()
    
    if(int(N)==0):
        last = "INSOMNIA"
        toCount = []
    else:
        toCount = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    j=1
    Nj=N
    while(len(toCount)!=0):
        
        for letter in list(Nj):
            if letter in toCount:
                toCount.remove(letter)
                last=Nj
        j=j+1
        Nj = str(int(N)*j)
        
        
    print "Case #{}: {}".format(i, last)