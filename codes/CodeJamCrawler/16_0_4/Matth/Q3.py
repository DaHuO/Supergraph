fin = open("in.in")
fout = open("out.out","w")
data = fin.read().split('\n')
T = int(data.pop(0))
recur_time = 1

def cal(k, C):
    global recur_time 
    result = (k-1)*K**(C-1)
    if C == 1: 
        result += 1
        return result
    if (recur_time < K) and (k != K): 
        recur_time += 1
        result += cal(k+1, C-1)
    else: result += 1
    return result
    
def candidates(K, C):
    global recur_time
    for k in range(1, K+1, C):
        recur_time = 1
        yield str(cal(k, C))

for i in range(1, T+1):
    K, C, S = data.pop(0).split()
    K = int(K)
    C = int(C)
    S = int(S)
    if (C * S < K): 
        print >>fout, "Case #%d: IMPOSSIBLE" % (i, )
        continue
    #if (K == 1): 
    #    print >>fout, "Case #%d: 1" % (i, )
    #    continue
    print >>fout, "Case #%d: " % (i, ) + " ".join(candidates(K, C))
fin.close()
fout.close()