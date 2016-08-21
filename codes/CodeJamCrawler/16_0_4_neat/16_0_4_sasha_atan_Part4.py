

numTests = int(raw_input())


for line in xrange(1, numTests + 1):
        L = [int(s) for s in raw_input().split(' ')]
        #print L
        
        solution = [i for i in range(1,L[0]+1)]
        
        print "Case #{}:".format(line), (str(solution)[1:-1]).replace(',','')