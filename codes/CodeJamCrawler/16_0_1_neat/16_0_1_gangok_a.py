def make_set(N):
    ret = set()
    while N > 0:
        ret.add(N%10)
        N = N / 10
    return ret

def run(N):
    init_N = N
    accset = set()
    firstset = make_set(N)
    accset = accset | firstset
    nowset = set()
    #print N, firstset, accset
    #while len(firstset ^ nowset) != 0:
    while True:
        if N == 0:
            break
        N = N + init_N
        nowset = make_set(N)
        accset = accset | nowset
        #print N, nowset, accset
        if len(accset) == 10:
            return N
    return "INSOMNIA"
    

infile = open("A-large.in", "r")
outfile = open("output.txt", "w")
data = infile.readlines()
T = int(data[0])
for t in range(T):
    N = int(data[t+1])
    ret = run(N)
    outfile.write("Case #" + str(t+1) + ": " + str(ret) + "\n")
    print str(N) + "result : " + str(ret)

infile.close()
outfile.close()
