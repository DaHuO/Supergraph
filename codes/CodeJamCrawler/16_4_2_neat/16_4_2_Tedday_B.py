level = __file__.split("\\")[-1][0]
file_is_small = True
attempt = 0
name = level+"-small-attempt"+str(attempt) if file_is_small else level+"-large"
input_file = file(name+".in","r")
output_file = file(name+"-output.txt","w")

def probability(c):
    L = len(c)+1
    probs = [[0.0 for i in xrange(L)] for j in xrange(L)]
    probs[0][0] = 1.0
    for i in xrange(1,L):
        C = c[i-1]
        for j in xrange(0,i):
            probs[i][j] += (1-C) * probs[i-1][j]
        for j in xrange(1,i+1):
            probs[i][j] += C * probs[i-1][j-1]
    return probs[L-1][L/2]

def select(array, subarray, k, index):
    if(index < len(array) and len(subarray) <= k):
        for p in select(array, subarray, k,index+1):
            yield p
        for p in select(array, subarray+[array[index]],k,index+1):
            yield p
    else:
        if(len(subarray) == k):
            #print subarray
            yield subarray    

def test_case():
    [N,K] = [int(i) for i in input_file.readline().split()]
    array = [float(i) for i in input_file.readline().split()]
    m = 0.0
    max_arr = []
    for arr in select(array,[],K,0):
        p = probability(arr)
        if(p > m):
            m = p
            max_arr = arr
    #print max_arr
    return m
    
T = int(input_file.readline())
for test in xrange(T):
    out = "Case #{0}: {1}".format(test+1,test_case())
    #print out
    output_file.write(out + "\n")
input_file.close()
output_file.close()
