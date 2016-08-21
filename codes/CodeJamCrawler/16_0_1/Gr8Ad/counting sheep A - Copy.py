intest = open("A-large.in", "r")
outtest = open("output1a.out", "w")
lines = intest.read()
llist = lines.splitlines()
tests = int(llist[0])
for i in range(1, tests+1):
    n = int(llist[i])
    if n == 0:
        outtest.write("Case #" + str(i) + ": INSOMNIA\n")
        continue
    cur = n
    notSeen = ["0","1","2","3","4","5","6","7","8","9"]
    x = 1
    while notSeen != []:
        curS = str(cur)
        for j in range(0, len(curS)):
            try:
                notSeen.remove(curS[j])
            except ValueError:
                pass
        x += 1
        cur = n*x
    if i == tests:
        outtest.write("Case #" + str(i) + ": " + curS)
    else:
        outtest.write("Case #" + str(i) + ": " + curS + "\n")
outtest.close()
