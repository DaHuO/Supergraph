import os

f = open("A-large.in", 'r')
ff = open("ans.txt", 'w')
n = int(f.readline())
for p in range(n):
    startN = long(f.readline())
    if startN == 0:
        ff.write("Case #%d: INSOMNIA\n" % (p + 1))
        continue
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    enc = 10
    pos = 1
    while enc != 0:
        modN = startN * pos
        while modN != 0:
            i = modN % 10
            modN /= 10
            if arr[i] == 0:
                arr[i] = 1
                enc -= 1
                if enc == 0:
                    break
        if enc == 0:
            break
        else:
            pos += 1
    ff.write("Case #%d: %d\n" % (p + 1, startN * pos))
ff.close()
f.close()