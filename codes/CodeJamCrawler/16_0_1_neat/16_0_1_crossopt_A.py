from sys import *

fin = open("a4.in", "r")
fout = open("a.out", "w")

t = int(fin.readline())
for i in range(1, t + 1):
    n = int(fin.readline())
    print("Case #", i, ": ", end = '', sep = '', file = fout)
    if n < 1:
        print("INSOMNIA", file = fout)
    else:
        used = [0 for i in range(10)]
        k = 0
        while sum(used) < 10:
            k += n
            cnt = k
            while cnt > 0:
                used[cnt % 10] = 1
                cnt //= 10
        print(k, file = fout)
        
fout.close()