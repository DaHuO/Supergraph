def seenall(seen, digs):
    return all([i in seen for i in digs])

def findnum(n, digs, case_num, out):
    seen = {}
    multiplier = 0
    if n is 0:
        out.write("Case #%d: INSOMNIA\n" % case_num)
    else:
        while not seenall(seen, digs):
            multiplier += 1
            for s in str(n * multiplier): seen[s] = True
        printnum(n * multiplier, case_num, out)
        print(seen)
    case_num += 1

def printnum(n, case_num, out):
    out.write("Case #%d: %d\n" % (case_num, n))

def main():
    fp = input()
    f = open(fp, 'r')
    out = open(fp.split('.')[0] + '.out', 'w')
    T = int(f.readline())
    ns = [int(f.readline()) for i in range(T)]

    case_num = 1

    digs = [str(i) for i in range(10)]
    for n in ns:
        findnum(n, digs, case_num, out)
        case_num += 1

main()
