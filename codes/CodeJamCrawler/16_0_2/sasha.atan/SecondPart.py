def to_array(s):
    ans = []
    for i in s:
        if i=='+':
            ans.append(1)
        else:
            ans.append(0)
    return ans  
    
def numToFix(L):
    swaps=0;
    for i in range(len(L)-1):
        if L[i]!=L[i+1]:
            swaps+=1
    return swaps
    
    
numTests = int(raw_input())

for line in xrange(1, numTests + 1):
        s = raw_input()
        
        L = to_array(s)

        solution = numToFix(L)
        if L[len(L)-1]==0:
            solution+=1
        #endroutine
        print "Case #{}: {}".format(line, solution)
        
