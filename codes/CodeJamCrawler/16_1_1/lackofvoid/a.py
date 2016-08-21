import sys

fn = sys.argv[1]

with open(fn) as f:
    lines = f.read().splitlines() # removes trailing \n in each line

T = int(lines[0])
output = ""

for i in range(1,T+1):
    S = lines[i]
    last = S[0]
    for l in S[1:]:
        if l >= last[0]:
            last = l+last
        else:
            last = last + l
    print("Case #%i: %s" % (i, last))
