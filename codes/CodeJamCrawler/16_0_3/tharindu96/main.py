FILE_NAME = "C-small-attempt0";

def numInBaseList(num, base):
    l = []
    while num:
        l.append(str(num % base))
        num /= base
    return l

def numInBase(num, base):
    l = []
    while num:
        l.append(str(num % base))
        num /= base
    l.reverse()
    l = "".join(l)
    return int(l)

def binInBase(num, base):
    num = str(num)
    num.split()
    l = len(num)
    n = 0
    for i, val in enumerate(num):
        n += int(val) * (base ** (l - (i + 1)))
    return n

def isPrime(num):
    if num == 1:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def checkIfValid(num):
    nums = []
    for i in xrange(2, 11):
        n = binInBase(num, i)
        nums.append(n)
        if isPrime(n):
            return False
    return nums

def getBinListList(N):
    l = []
    i = 2
    while True:
        b = numInBase(i, 2)
        blist = str(b)
        if(len(blist) > N): break;
        if int(blist[0]) == 1 and int(blist[-1]) == 1 and len(blist) == N:
            l.append(b)
        i += 1
    return l

def getFactor(num):
    i = 2
    while i*i <= num:
        if num % i == 0:
            return i
        i += 1
    return 1

def processAndGetResult(line):
    N, J = line.split()
    J = int(J)
    N = int(N)
    return getResult(J, N)

def getResult(J, N):
    numList = getBinListList(N)
    out = []
    for num in numList:
        if J == 0: break;
        nums = checkIfValid(num)
        if not nums == False:
            lout = str(num)
            for i in nums:
                fac = getFactor(i)
                lout += " " + str(fac)
            out.append(lout)
            J -= 1
    return out

def main():
    with open("./"+FILE_NAME+".in", "r") as f:
        with open("./"+FILE_NAME+".out", "w") as r:
            first = True
            j = 0
            for line in f:
                if first == True:
                    first = False
                    continue
                j += 1
                res = processAndGetResult(line)
                r.write("Case #1:\n")
                for l in res:
                    r.write(l+"\n")

if __name__ == '__main__':
    main()
