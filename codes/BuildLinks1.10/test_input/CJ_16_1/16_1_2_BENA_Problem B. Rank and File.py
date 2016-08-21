"""
Within every row of the grid,
the soldiers' heights must be in strictly increasing order,
from left to right.

Within every column of the grid,
the soldiers' heights must be in strictly increasing order,
from top to bottom.

"""
def solve(soldierList, n):
    map = {}
    for s in soldierList :
        if str(s) in map:
            map[str(s)] = map[str(s)] + 1
        else:
            map[str(s)] = 1

    nums = []
    for k, v in map.items():
        if v % 2:
            nums.append(int(k))

    #print(nums)
    nums.sort()

    return nums


def main():
    #inputFile = "B-small-practice.in"
    #inputFile = "B-sample.in"
    #inputFile = "B-small-attempt1.in"
    inputFile = "B-large.in"
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    testCase = int(inpf.readline())
    for case in range(testCase):
        n = int(inpf.readline())
        soldierList = []
        for i in range(n*2 - 1):
            soldier = [int(x) for x in inpf.readline().strip().split(' ')]
            for s in soldier:
                soldierList.append(s)
        rst = solve(soldierList, n)
        result = 'Case #{}: {}\n'.format(case+1, ' '.join(str(v) for v in rst))
        print(result, end="")
        outf.write(result)
    inpf.close()
    outf.close()

if __name__ == "__main__":
    main()


