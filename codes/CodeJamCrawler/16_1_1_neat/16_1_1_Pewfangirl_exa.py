inf = open("in.txt", "r")
ouf = open("out.txt", "w")

for case in range(int(inf.readline())):
    s = inf.readline().strip()
    res = ""
    for c in s:
        if not res or ord(res[0]) <= ord(c):
            res = c + res
        else:
            res = res + c
    ouf.write("Case #" + str(case + 1) + ": " + res + "\n")

inf.close()
ouf.close()