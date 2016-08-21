import sys

def solve(K, C, S):
    #print K, C, S
    if S * C < K:
        return "IMPOSSIBLE"
    res = []
    j = 0

    for i in xrange(S):
        n = 0
        t = 0
        while t < C and j < K ** C and n + j * (K ** (j % C)) < K ** C:
            #print "adding", j * (K ** (j % C)), "to", n, "=", n + j * (K ** (j % C))
            n += j * (K ** (j % C))
            j += 1
            t += 1
        if n not in res:
            if not(t == 0 and len(res) > 0):
                res.append(n)
    #print ""
    return [str(n+1) for n in res]

#        for j in xrange(i * C, (i + 1) * C):
#            if n + j * (K ** j) >= K ** C:
#                break
#            n += j * (K ** j)
#        if n >= K ** C:
#            print n, K ,C, S
#            break
#        res.append(str(n + 1))

input_file = open(sys.argv[1], "r")
output_file = open(sys.argv[2], "w")

T = int(input_file.readline().strip())
strings = input_file.readlines()
results = []
for s in strings:
    (K, C, S) = s.strip().split(' ')
    results.append(solve(int(K), int(C), int(S)))

for i in xrange(T):
    if results[i] == "IMPOSSIBLE":
        output_file.write("Case #{0}: {1}\n".format(i+1, results[i]))
    else:
        s = " ".join(results[i])
        output_file.write("Case #{0}: {1}\n".format(i+1, s))

input_file.close()
output_file.close()