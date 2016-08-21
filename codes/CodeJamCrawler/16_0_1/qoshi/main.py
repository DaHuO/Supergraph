def check(x):
    ret = {}
    while x>0:
        ret[x%10] = True
        x = x//10
    return ret

def solve(x):
    t = {i:False for i in range(0,10)}
    found = 0
    if x==0:
        return "INSOMNIA"
    k = 0
    while (found < 10):
        tmp = check(k)
        for i in tmp:
            if t[i] == False:
                found += 1
                t[i] = True
        if found == 10:
            return k
        k += x

t = int(input())
for i in range(1,t+1):
    x = int(input())
    print "Case #%d:"%i,solve(x)




