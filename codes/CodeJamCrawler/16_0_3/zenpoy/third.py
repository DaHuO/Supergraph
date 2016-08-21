import sys
import random
import math
import json
import os.path
import pickle

mem_file = 'memory.p'
if (os.path.isfile(mem_file)):
    with open(mem_file, 'rb') as infile:
        memory = pickle.load(infile)
else:
    memory = {}

def get_ntd(c):
    i = 2
    # while (i < math.sqrt(c) + 1):
    while (i < 100):
        if (c == (c / i) * i):
            return i
        i += 1
    return None

def solve(n, j):
    if ((n, j) in memory):
        results = json.loads(memory[(n,j)])
    else:
        results = {}
    results_disp = []
    garbage_can = set()
    if (not results):
        for i in xrange(j):
            proof = []
            while (True):
                coinjam_candidate = '1' + ''.join(random.choice(['0', '1']) for _ in range(n - 2)) + '1'
                if coinjam_candidate in garbage_can:
                    continue;
                garbage_can.add(coinjam_candidate)
                # print coinjam_candidate
                proof = []
                for b in xrange(2, 11):
                    k = get_ntd(int(coinjam_candidate, base=b))
                    # print k
                    if not k:
                        break
                    proof.append(k)
                if (len(proof) == 9):
                    results[coinjam_candidate] = proof
                    break

        memory[(n, j)] = json.dumps(results)

    for r, p in results.iteritems():
        results_disp.append(str(r) + " " + " ".join(str(x) for x in p))

    return results_disp


results = []

with open(sys.argv[1]) as f:
    T = int(f.readline().rstrip())
    for i in xrange(T):
        line = f.readline().rstrip().split(" ")
        N = int(line[0])
        J = int(line[1])
        results.append(solve(N, J))

for i, r in enumerate(results):
    print "Case #{0}:\n{1}".format(i + 1, "\n".join(r))

with open(mem_file, 'wb') as outfile:
    pickle.dump(memory, outfile)
