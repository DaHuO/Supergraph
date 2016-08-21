
import numpy as np

def to_array(n):
    return [int(i) for i in str(n)]

def get_input():
    numTests = int(raw_input())
    inputs = []
    for i in xrange(1, numTests + 1):  
        inputs.append([int(s) for s in raw_input().split(" ")])
    return [numTests, inputs]

numTests = int(raw_input())

for line in xrange(1, numTests + 1):
        N = int(raw_input())

        NotSeen = [0,1,2,3,4,5,6,7,8,9]

        if N==0:
            solution = "INSOMNIA"
        else:
            i=0
            while(NotSeen != []):
                i+=1;
                n = to_array(i*N)
                for k in n:
                    if k in NotSeen:
                        NotSeen.remove(k)
            solution = i*N;
        
        #endroutine
        print "Case #{}: {}".format(line, solution)




