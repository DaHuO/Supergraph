import sys
import itertools

swap = {"+":"-", "-":"+"}

def rmDup(info):
    unique = (i[0] for i in itertools.groupby(info))
    return "".join(unique)

def doStuff(info):
    plus = 0
    minus = 0
    count = 0
    info = rmDup(info) 
    while (info != '+' and info != '-' and info != "+-"):
        info = rmDup(info) 
        if info[-1] == '+':
            info = info[:-1]
        if info[0] == '-':
            tmp = list(info)
            tmp[0] = '+'
            info = "".join(tmp)
        elif info[0] == '+':
            info = "".join(swap.get(c, c) for c in info)
   
        count += 1
    
    if info == "+-":
        count += 2
    elif info == "-":
        count += 1

    return count

def main():
    f = sys.stdin
    case = 0
    for line in f:
        if case != 0:
            print "Case #" + str(case) + ": " + str(doStuff(line.strip()))
        case += 1


main()
