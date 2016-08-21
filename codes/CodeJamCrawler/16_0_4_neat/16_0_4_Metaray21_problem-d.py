
data = open("D-large.in").read().split()
data = map(int, data)
n = data[0]
data = zip(data[1::3], data[2::3], data[3::3])
answ = []

for k,c,s in data:
    ca = []
    found = False
    j = 0
    for i in xrange(s):
        pos = 0
        for x in xrange(c):
            pos = pos*k + j
            if j < k - 1:
                j += 1
            else:
                found = True
        ca.append(str(pos+1))
        if found:
            break

    if found:
        answ.append(" ".join(ca))
    else:
        answ.append("IMPOSSIBLE")

with open("D-large.out",'w') as f:
    for i,o in enumerate(answ):
        f.write("Case #{}: {}\n".format(i+1, o))
