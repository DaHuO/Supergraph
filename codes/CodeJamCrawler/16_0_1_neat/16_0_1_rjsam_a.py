import sys

def main():
    cCnt = int(sys.stdin.readline().strip())
    for i in range(cCnt):
        iNum = int(sys.stdin.readline().strip())

        if iNum == 0:
            print("Case #{0}: {1}".format(i+1, "INSOMNIA"))
        else:
            j = 1
            nStr = list("0123456789")
            while nStr:
                nNum = iNum*j
                nNum = list(str(nNum))
                nStr = [x for x in nStr if x not in nNum]
                j += 1

            print("Case #{0}: {1}".format(i+1, ''.join(nNum)))

    return 0

main()
