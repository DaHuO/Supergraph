__author__ = 'anton'

def Count():
    f = open("oppa.txt", "r")
    output = open("output.txt", "w")
    f.readline()
    cnt = 0
    for s in f.readlines():
        print s
        cnt += 1
        n = int(s.strip())
        if n == 0:
            output.write("Case #" + str(cnt) + ": INSOMNIA\n")
            continue
        oppa = [False] * 10
        res = 0
        while True:
            if oppa == [True] * 10:
                break
            res += 1
            tmp = res * n
            while tmp != 0:
                oppa[tmp%10] = True
                tmp /= 10
        output.write("Case #" + str(cnt) + ": " + str(res * n) + "\n")
    output.close()


Count()