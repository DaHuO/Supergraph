import fileinput

def strip(l):
    if len(l)>0 and l[-1]=='\n': return l[:-1]
    else: return l

def solve(K, C, S):
    return range(1, K+1)

f = fileinput.input()
nc = int(f.next())

for ic in range(1, nc+1):
    line = f.next()
    line = strip(line)
    line = line.split()
    line = [int(e) for e in line]
    ans  = solve(line[0], line[1], line[2])
    ans  = [str(e) for e in ans]
    ans  = " ".join(ans)
    print "Case #%d: %s" % (ic, ans)
