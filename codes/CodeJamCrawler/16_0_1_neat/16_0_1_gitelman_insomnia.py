


def getDigits(num):
    toReturn = set()
    while num:
        toReturn.add(num%10)
        num = num/10
    return toReturn

def lastNumber(N):
    if N == 0:
        return "INSOMNIA"
    else:
        seenSoFar = set()
        currNum = N
        while True:
            toAdd = getDigits(currNum)
            seenSoFar = seenSoFar.union(toAdd)
            if len(seenSoFar) == 10:
                return currNum
            currNum += N

def main():
    T = int(raw_input())
    for i in range(1, T+1):
        N = int(raw_input())
        ans = lastNumber(N)
        print "Case #{}: {}".format(i, ans)



if __name__ == "__main__":
    main()


