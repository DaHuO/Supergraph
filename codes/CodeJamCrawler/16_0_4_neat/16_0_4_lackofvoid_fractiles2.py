import sys

fn = sys.argv[1]

with open(fn) as f:
    lines = f.read().splitlines() # removes trailing \n in each line

T = int(lines[0])
output = ""

for i in range(1,T+1):
    kcs = lines[i].split(" ")
    K = int(kcs[0])
    C = int(kcs[1])
    S = int(kcs[2])
    if S < K:
        out = "IMPOSSIBLE"
    elif S == K:
        out = " ".join([ str(i+1) for i in range(S) ])

    print("Case #%i: %s" % (i,out))
