from itertools import combinations
import time

fin = open('A-large.in','r')
lines = fin.readlines()
fin.close()

names = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def islegal(conf):
    # return true iff no element of conf is > sum(conf)/2
    for party in conf:
        if party > sum(conf)/2:
            return False
    return True

def solve(conf):
    # iterate through possible next steps, greedily pick the first that works
    if sum(conf)==0:
        return []
    for comb in combinations(range(N), 2):
        if conf[comb[0]]==0 or conf[comb[1]]==0:
            continue
        nextconf = conf[:]
        nextconf[comb[0]] -= 1
        nextconf[comb[1]] -= 1
        if islegal(nextconf):
            therest = solve(nextconf)
            if therest != None:
                return [names[comb[0]]+names[comb[1]]] + therest
            
    for i in range(len(conf)):
        if conf[i] == 0:
            continue
        nextconf = conf[:]
        nextconf[i] -= 1
        if islegal(nextconf):
            therest = solve(nextconf)
            if therest != None:
                return [names[i]] + therest
    
    return None

t0 = time.time()
T = int(lines.pop(0))
fout = open("senators_out.txt",'w')
for i in range(T):
    N = int(lines[2*i])
    conf = [int(x) for x in lines[2*i+1].strip().split()]
    plan = solve(conf)
    plan = " ".join(plan)
    fout.write("Case #%d: %s\n" % (i+1, plan))

fout.close()

print "Time:", time.time()-t0
