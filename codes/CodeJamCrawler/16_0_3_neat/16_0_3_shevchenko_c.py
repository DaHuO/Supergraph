xx = [0] * 10000
ps = []
for i in range(2,10000):
    if xx[i] == 0:
        ps.append(i)
        for j in range(i, 10000, i):
            xx[j] = 1

N = 32
J = 500

print "Case #1:"
X = (1<<(N-1))+1
while(True):
    seq = []
    x = X
    while(x>0):
        seq.append(x%2)
        x = x/2

    divs = []
    for b in range(2,11):
        num = 0
        div = -1
        for i in range(N):
            num = num + seq[i] * (b**i)
        for p in ps:
            if num%p == 0:
                div = p
                break
        if div == -1:
            divs = None
            break
        divs.append((num,div))

    if divs is not None:
        binStr = ''
        for i in range(N-1, -1, -1):
            binStr = binStr + str(seq[i])
        print binStr,
        for (num,div) in divs:
            print div,
        print ''
        J = J - 1
    if J == 0:
        break
    X = X+2
