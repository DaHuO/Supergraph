import random

file = open("./C-small-attempt0.in")
limit = int(file.readline())
index = 1

def is_prime(q, k = 50):
    if q == 2:
        return True
    if q < 2 or q&1 == 0:
        return False

    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1

    for i in xrange(k):
        a = random.randint(1, q - 1)
        t = d
        y = pow(a, t, q)
        while t != q - 1 and y != 1 and y != q - 1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q - 1 and t&1 == 0:
            return False
    return True

while limit > 0:
    line = file.readline()
    N, J = (int(s) for s in line.split())
    count = 0
    binlist = []
    num = 0
    while count < J:
        #randbin = [str(random.randint(0,1)) for b in xrange(N - 2)]
        #randbin.insert(0, "1")
        #randbin.append("1")
        #randbin = "".join(randbin)
        padding = '0' * (N - 2 - len(format(num, 'b')))
        randbin = "1" + padding + format(num, 'b') + "1"
        if len(randbin) > N:
            break
        binlist.append([randbin, []])
        for i in xrange(2, 11):
            if not is_prime(int(randbin, i)):
                binlist[count][1].append(int(randbin, i))
                if i == 10 and len(binlist[count][1]) == 9:
                    count += 1
            else:
                binlist.pop(count)
                break
        num += 1
    print("Case #%d:" % index)
    for i in xrange(J):
        print("%s" % binlist[i][0]),
        for j in xrange(9):
            for div in xrange(2, binlist[i][1][j]):
                if binlist[i][1][j] % div == 0:
                    print("%d" % div),
                    break
        print("")
    limit -= 1
    index += 1

