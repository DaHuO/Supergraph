
def count(ss):
    if ss == 0:
        return -1
    s = 1

    flag = [i for i in range(10)]
    while s < 200:
        n = s * ss
        s += 1
        for j in str(n):
            if int(j) in flag:
                for k in range(len(flag)):
                    if flag[k] == int(j):
                        flag.pop(k)
                        break
        if len(flag) == 0:
            return n


f = open("A-large.in","r+")
w = open("output","w+")
f.readline()
idx = 0
for row in f.readlines():
    idx += 1
    result = count(int(row))
    if result == -1:
        result = "INSOMNIA"
    w.write("Case #"+str(idx)+": "+str(result)+"\n")