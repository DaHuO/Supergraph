import math



def run(InputK, InputC, InputS):
    
    h = int(math.pow(InputK, InputC - 1))
    d = 1
    result = ''
    for i in xrange(0, InputK):
        if len(result) != 0:
            result += ' '
        result += str(int(d + i * h))
    return result    

f = open("D-small-attempt3.in", "r")

T = int(f.readline())

for x in range(0, T):
    readline = f.readline()
    K, C, S = readline.strip().split(' ')
    K = int(K)
    C = int(C)
    S = int(S)
    print "Case #" + str(x+1) + ": " + str(run(int(K), int(C), int(S)))
    
