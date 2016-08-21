
def findMax(n):
    maxVal = 0
    maxIdx = 0
    for index, item in enumerate(n):
        if (item >= maxVal):
            maxVal = item
            maxIdx = index
    if maxVal == 0: return -1
    return maxIdx

def getSenator(n):
    return str(unichr(65+n))

def sum2(n):
    total = 0
    for val in n:
        total += val
    if total == 2: return True
    return False


def solve(n):
    rst = []
    while True:
        thisSenator = ""
        maxIdx1 = findMax(n)
        if maxIdx1 < 0 :
         return rst

        n[maxIdx1] -= 1
        thisSenator = getSenator(maxIdx1)

        if sum2(n) == True:
            rst.append(thisSenator)
            continue

        maxIdx2 = findMax(n)
        if maxIdx2 < 0:
            rst.append(thisSenator)
            return rst

        n[maxIdx2] -= 1
        thisSenator += getSenator(maxIdx2)
        rst.append(thisSenator)



def main():
    #inputFile = "A-small-attempt.in"
    inputFile = "A-large (2).in"
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    testCase = int(inpf.readline())
    for case in range(testCase):
        parties = int(inpf.readline())
        n = [int(x) for x in inpf.readline().strip().split(' ')]
        rst = solve(n)


        result = 'Case #{}: {}\n'.format(case+1,  ' '.join(rst))
        #print n
        print result,
        outf.write(result)
    inpf.close()
    outf.close()

def main2():
    print str(unichr(65))
    return False


if __name__ == "__main__":
    main()
    #main2()


