import sys
orig_stdout = sys.stdout
f = file('ou.txt', 'w')
sys.stdout = f

for i in range(input()):

    l = []
    N = int(input())
    for j in range(2*N-1):
        n = map(str, raw_input().strip().split())
        l.append(n)
    x = set(l[0])
    for j in range(1, len(l)):
        x = x^set(l[j])
    k = [int(j) for j in x]
    k.sort()
    l = [str(j) for j in k]
    print "Case #%s: %s"%(i+1," ".join(l))


sys.stdout = orig_stdout
f.close()
