inf = open("in.txt", "r")
ouf = open("out.txt", "w")

for case in range(int(inf.readline())):
    n = int(inf.readline())
    m = n
    enc = [0] * 10
    sleep = False
    cnt = 0
    while not sleep and cnt < 1000:
        for d in str(n):
            enc[int(d)] = True
        p = 0
        for i in range(10):
            if enc[i]:
                p += 1
        if p == 10:
            sleep = True
        
        n += m
        cnt += 1
    if m == 0:
        ouf.write("Case #" + str(case + 1) + ": INSOMNIA\n")
    else:
        ouf.write("Case #" + str(case + 1) + ": " + str(m * cnt) + "\n")

inf.close()
ouf.close()