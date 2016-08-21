__author__ = 'anton'

def Doit():
    f = open("oppa.txt", "r")
    output = open("output.txt", "w")
    f.readline()
    cnt = 0
    for s in f.readlines():
        s = s.strip() + '+'
        print s
        cnt += 1
        prev = s[0]
        res = 0
        for c in s:
            if prev != c:
                print prev, c
                res += 1
            prev = c
        output.write("Case #" + str(cnt) + ": " + str(res) + "\n")
        print "oppa"
    output.close()


Doit()