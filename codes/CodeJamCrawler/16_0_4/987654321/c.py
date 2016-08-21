import math

f = open('D-small-attempt4.in', 'r')




def test_case(a):
    a =  a.rstrip().split(" ")
    if len(a) < 3:
        return
    
    k = int(a[0])
    c = int(a[1])
    s = int(a[2])
    
    #print k,c,s
    if s < k/c:
        return "IMPOSSIBLE"
    else:
        solutions = []
    
        x = 1
        while x <= k:
            sol = x
            for j in range(x+1,min(x+c,k+1) ):
                #print "x=" + str(x) + "j=" + str(j), 
                m = int(math.pow(k,j - x))
                #print "multipplyer  " + str(m),
                sol = sol + (j-1) * m
                #print "sol  " + str(sol)
                
            x = x + c
            solutions.append(sol)
            
            
        return solutions
		
cases = int(f.readline())	
#print cases
line = 1
case = 0
while line:
    
    case = case + 1
    line = f.readline()
    out = test_case(line )
    
    if out == "IMPOSSIBLE":
        print "Case #" + str(case) + ":",
        print out
    else:
        if (out != None):
            if len(out) != len(out):
                print "MISTAKE"
            print "Case #" + str(case) + ":",
            for j in out:
                print str(j),
            print

