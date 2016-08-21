#Code by Lilli Christoph 2016

#!usr/bin/python


import sys
num_cases = int(sys.stdin.readline())

for i in range(num_cases):
    raw_data = [int(x) for x in sys.stdin.readline().split()]
    K = raw_data[0] #length of original artwork
    city = raw_data[1] #city=C=complexity
    sMax = raw_data[2] #number of tiles that can be revealed
    dusted = []
    
    #solution for 'small' case is trivial
    #When S==K, can always be solved, because we can reveal the orig K tiles
    #this solution reveals those K tiles
    if(sMax == K):
        for x in range(0, pow(K,city), pow(K,city-1)):
            dusted.append(x+1)
    
    else:
        if(city == 1):
            #sMax < K and the artwork has not been iterated
            #So, we can't reveal all the tiles and therefore can't know
            print 'Case #{}: {}'.format(i+1, "IMPOSSIBLE")
            continue
    print 'Case #{}: {}'.format(i+1, ' '.join(str(j) for j in dusted))
