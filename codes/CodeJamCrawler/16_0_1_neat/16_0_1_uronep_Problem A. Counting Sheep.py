
nums = {}

def addNums(n):
    digits = list(str(n))
    for k in digits:
        nums[str(k)] = 1

def isFallAsleep():
    for i in range(10):
        if not str(i) in nums:
            return False
    return True


def solve(n):
    nums.clear()
    if n == 0:
        return False
    for i in range(1, 1001):
        multiply = n * i
        addNums(multiply)
        rst = isFallAsleep()
        if rst == True:
            return multiply
    return False


def main():
    #inputFile = "A-small-attempt.in"
    inputFile = "A-large (1).in"
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    testCase = int(inpf.readline())
    for case in range(testCase):
        #n = [int(x) for x in inpf.readline().strip().split(' ')]
        n = int(inpf.readline())
        rst = solve(n)

        if rst == False:
            result = 'Case #{}: INSOMNIA\n'.format(case+1)
        else:
            result = 'Case #{}: {}\n'.format(case+1,  rst)
        #print n
        print result,
        outf.write(result)
    inpf.close()
    outf.close()

def main2():
    case = 0
    n = 1256
    rst = solve(n)
    if rst == False:
        result = 'Case #{}: INSOMNIA\n'.format(case+1)
    else:
        result = 'Case #{}: {}\n'.format(case+1,  rst)
    print n
    print result,


if __name__ == "__main__":
    main()
    #main2()


