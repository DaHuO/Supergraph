import sys, os

def countsheep(n):
    if n == 0:
        return "INSOMNIA"
    target = (1 << 10) - 1
    mult = 0
    seen = 0

    while target - seen != 0:
        mult += 1
        current = mult*n
        while(current != 0):
            seen |= (1 << (current%10))
            current = current // 10
    return mult*n


def main1():
    with open("outpy.txt", "w") as ins:
        for x in range(1, 10001):
            soln = countsheep(x)
            print(soln)
            ins.write(str(soln))
            ins.write("\n")


def contestMain():
    case = 1
    with open(sys.argv[1], "r") as ins:
        with open("outpy.txt", "w") as out:
            ins.readline()
            for line in ins:
                out.write("Case #%d: " % case)
                out.write(str(countsheep(int(line))))
                out.write("\n")
                case += 1

def debugMain():
    for x in range(1998, 2002):
        soln = int(countsheep(x))

if __name__ == "__main__":
    debugMain()
    printdebug = False
    #main1()
    contestMain()

"""

  101
   11
 11
   11 
    1 * 3 * 5


"""



