fin = open("in.in")
fout = open("out.out","w")
data = fin.read().split('\n')
fin.close()
T = int(data[0])
data.pop(0)
def check(a):
    """
    a is the integer to be checked
    """
    while(a!=0):
        seen[a % 10] = True
        a /= 10
        
for i in range(1, T+1):
    N = int(data.pop(0))
    if (N == 0): 
        print >>fout, "Case #%d: INSOMNIA" % (i,)
        continue
    seen = [False] * 10
    cur = 0
    while(sum(seen)!= 10):
        cur += N
        check(cur)
    print >>fout, "Case #%d: %d" % (i, cur)
fout.close()