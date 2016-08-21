import time

def work(n):
    d = [0]*10
    O = n
    i = 1
    noc = 0
    while True:
        n = O * i
        c, d = check(str(n), d)
        if sum(d) == 10:
            return n
        if c > 0:
            noc = 0
        else:
            noc+=1
        if noc > 10000:
            return "INSOMNIA"

        i+=1
        
        

def check(s,d):
    c = 0
    for l in s:
        if d[int(l)] == 0:
            d[int(l)] = 1
            c += 1
    return [c, d]
    

startT = time.time()

a = open("A-large.in")
a = a.readlines()
N = int(a.pop(0))
        
for i in range(N):
    n = 0
    r = work(int(a.pop(0)))
    print "Case #"+str(i+1)+":", r

endT = time.time()

#print (endT - startT)