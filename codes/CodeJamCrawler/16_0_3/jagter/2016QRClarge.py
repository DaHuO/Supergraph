import numpy as np

ind = open("C-large.in", "r")
outd = open("C-large.out", "w")

T = int(ind.readline())

def newCoin(N, n):
    c = "1" + np.binary_repr(n,N - 2) + "1"
    return c

def findDivisor(n):
    i = 1
    while i < 10000:
        i += 1
        if n%i == 0: return i
    return 0

for i in range(1, T + 1):
    N, J = map(int, ind.readline().split())

    jamcoins = []
    divisors = np.zeros((J,9))
    j = 0
    
    while len(jamcoins) < J:
        IsJamCoin = True
        for k in reversed(range(2,11)):
            divisors[len(jamcoins),k - 2] = findDivisor(int(newCoin(N, j),k))
            if divisors[len(jamcoins),k - 2] == 0:
                IsJamCoin = False
                print "lets try next one"
                print newCoin(N,j) + " takes too long"
                break
        if IsJamCoin:
            jamcoins.append(newCoin(N,j))
            print len(jamcoins)
        j += 1
            
    outd.write("Case #" + str(i) + ":\n")
    for j in range(len(jamcoins)):
        outd.write(jamcoins[j])
        for k in divisors[j]:
            outd.write(" " + str(int(k)))
        outd.write("\n")

ind.close()
outd.close()

