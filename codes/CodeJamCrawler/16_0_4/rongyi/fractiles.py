def fractiles(k, c, s):
    res = []
    if k == s:
        indx = k ** (c - 1)
        for i in range(k):
            res.append(str(i * indx + 1))
    return res

t = int(input())

for i in range(1, t + 1):
    tmp = input()
    tmp = tmp.split(' ')
    k = int(tmp[0])
    c = int(tmp[1])
    s = int(tmp[2])
    res = fractiles(k, c, s)
    print("Case #" + str(i) + ": " + " ".join(res))
