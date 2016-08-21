inf = open("in.txt", "r")
ouf = open("out.txt", "w")

for case in range(int(inf.readline())):
    k, c, s = map(int, inf.readline().split())
    if s < k:
        ouf.write("Case #" + str(case + 1) + ": IMPOSSIBLE\n")
    else:
        ouf.write("Case #" + str(case + 1) + ": ")
        for i in range(1, k + 1):
            ouf.write(str(i) + " ")
        ouf.write("\n")

inf.close()
ouf.close()