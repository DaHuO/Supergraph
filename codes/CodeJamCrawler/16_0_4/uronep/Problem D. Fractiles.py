def solve(k, c, s):
    minTile = k + 1 - c

    if minTile < 1:
        minTile = 1

    if s < minTile:
        return False

    rst = []
    if c == 1:
        for i in range(1, k+1):
            rst.append(str(i))
    else:
        for i in range(minTile):
            rst.append(str((i+1)*k))

    return rst

def solve2(k,c,s):
    rst = []
    for i in range(1, s+1):
        rst.append(str(i))
    return rst


def main():
    #inputFile = "D-small-practice.in"
    inputFile = "D-small-attempt0 (2).in"
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    testCase = int(inpf.readline())
    for case in range(testCase):
        k, c, s = [int(x) for x in inpf.readline().strip().split(' ')]
        #n, j = [int(x) for x in inpf.readline().strip().split(' ')]
        #s = inpf.readline()
        rst = solve2(k, c, s)
        if rst == False:
            result = 'Case #{}: {}\n'.format(case+1, "IMPOSSIBLE")
        else:
            result = 'Case #{}: {}\n'.format(case+1, ' '.join(rst))

        print result,
        outf.write(result)
    inpf.close()
    outf.close()

def main2():
    rst = solve(6,3)
    print rst,


if __name__ == "__main__":
    main()
    #main2()
