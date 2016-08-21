
def find_num(x):
    if x==0:
        return 0
    k=[0]*10
    n = 0
    (q,r) = divmod(n,10)
    while sum(k)!=10:
        n += x
        (q,r)=divmod(n,10)
        k[r] = 1
        while q!=0 and sum(k)!=10:
            (q,r)=divmod(q,10)
            k[r] = 1
    return n

T = int(raw_input())

for a in range(1,T+1):
    x = int(raw_input())
    res = find_num(x)
    if x == 0:
        print "Case #%d: INSOMNIA" % (a)
    else:
        print "Case #%d: %d" % (a, res)

        
        


