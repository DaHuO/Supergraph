
f = open("B-large.in", "r")
o = open("B-large.out", "w")

T = int(f.readline().strip())

for j in range(1, T+1):
    o.write("case #{}: ".format(j))
    line = f.readline().strip()
    L = []
    for i in line:
        if i == '+':
            L.append(1)
        elif i == '-':
            L.append(0)
        else:
            raise Exception("aksdalksd")
    L.reverse()
    count = 0
    while 0 in L:
        rev = False
        for k in range(len(L)):
            if L[k] == 0 and rev == False:
                rev = True
                L[k] = 1
            elif rev == True:
                L[k] = L[k] ^ 1
        count += 1
    o.write("{}\n".format(count))

f.close()
o.close()