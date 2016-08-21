import sys


def doStuff(info):
    
    if (info == 0):
        return "INSOMNIA"

    x = range(0, 11)
    count = 0
    N = 2
    base = info
    while(True):

        numString = str(info)
        
        
        for char in numString:
            loc = int(char)
            if x[loc+1] != 0:
                x[loc+1] = 0
                count += 1
        if count != 10:    
            info = base * N
            N += 1
        else:
            break

    return str(info)

def main():
    f = sys.stdin
    case = 0
    for line in f:
        if case != 0:
            print "Case #" + str(case) + ": " + doStuff(int(line))
        case += 1


main()
