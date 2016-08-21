def asleep(n):
    if n==0:
        return 'INSOMNIA'
    # seen digits:
    digs = [] #seen digits:
    s = n # current number
    i = 1 # muliplier
    while True:
        while s>0:
            d = s % 10
            if digs.count(d)==0:
                digs.append(d)
            s /= 10
        if len(digs)==10:
            return str(n*i)
        i+=1
        s=n*i

f = open('input.txt', 'r')
T = int(f.readline())
tcs = []

for i in range(T):
    tcs.append(int(f.readline()))

f.close()
f = open('output.txt', 'w')
for i in range(T):
    f.write("Case #%s: %s\n" % (i+1, asleep(tcs[i])))
f.close()


