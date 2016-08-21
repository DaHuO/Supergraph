T = raw_input()
T = int(T)
lst = []

for i in range(0, T):
    N = raw_input()
    lst.append(N)

i = 1
for n in lst:
    if n == "0":
        print "Case #%d%s" % (i,": INSOMNIA")
        continue
    goSleep = set(n)
    iter = 2
    out = int(n)
    while(len(goSleep) != 10):
        out = int(n) * iter
        n1 = str(out)
        goSleep.update(set(n1))
        iter = iter + 1
    i = i+1
    print "Case #%d%s %d" % (i,":",out)