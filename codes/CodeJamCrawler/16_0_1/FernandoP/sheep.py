
def isFull(v):
    for i in range(10):
        if v[i] == 0:
            return False
    return True

def fill(n,v):
    while(n != 0):
        nc = n % 10
        v[nc] = 1
        n /= 10


ninput = int(raw_input())
for i in range(ninput):
    val = int(raw_input())
    r = "INSOMNIA"
    vec = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    if val != 0:
        end = 0
        candid = 0
        end = isFull(vec)
        r = 0
        while (end == False):
            candid += val
            r = candid
            fill(candid,vec)
            end = isFull(vec)
    print "Case #"+str(i+1)+":",
    print r




