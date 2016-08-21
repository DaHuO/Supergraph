##f = open('test.in')
f = open('D-small-attempt0.in')
##f = open('D-large.in')
f2 = open('file.txt','w')
f.readline()
i = 0
for l in f:
    i += 1
    K, C, S = [int(x) for x in l.split()]
    if(K != S):
        print("Case #" + str(i) + ": IMPOSSIBLE",file=f2)
        continue
    n = range(1, S + 1)
    print("Case #" + str(i) + ": " + " ".join(str(x) for x in n),file=f2)
f.close()
f2.close()
