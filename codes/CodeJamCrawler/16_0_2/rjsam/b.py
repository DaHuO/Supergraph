import sys

def main():
    cCnt = int(sys.stdin.readline().strip())
    for i in range(cCnt):
        cList = list(sys.stdin.readline().strip())

        if len(set(cList)) == 1:
            if cList[0] == "+":
                print("Case #{0}: {1}".format(i+1, 0))
            else:
                print("Case #{0}: {1}".format(i+1, 1))
        else:
            j = 0
            while len(set(cList)) != 1:
                cList = flip(cList)
                j += 1

            if cList[0] == "+":
                print("Case #{0}: {1}".format(i+1, j))
            else:
                print("Case #{0}: {1}".format(i+1, j+1))

    return 0

def flip(iList):
    iList = list(iList)
    if iList[-1] == "+":
        i = 1
        while iList[-i] == "+":
            i += 1
        iList = iList[0:-(i-1)]

    if iList[0] == "+":
        i = 0
        while iList[i] == "+":
            i += 1
        for j in range(i):
            iList[j] = "-"
        return ''.join(iList)

    iList = ["+" if iList[i] == "-" else "-" for i in range(len(iList))]

    return ''.join(iList)

main()
