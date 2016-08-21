def main():
    fp = input()
    f = open(fp, 'r')
    out = open(fp.split('.')[0] + '.out', 'w')
    n = int(f.readline())
    stacks = [list(l) for l in f.read().split('\n')[:-1]]
    case_num = 1
    for stack in stacks:
        flips = 0
        num_cakes = len(stack)
        for i in range(num_cakes - 1, -1, -1):
            if stack[i] is '-':
                flip(stack, i)
                flips += 1
        printnum(flips, case_num, out)
        case_num += 1

def printnum(n, case_num, out):
    out.write("Case #%d: %d\n" % (case_num, n))

# flip up to n
def flip(stack, n):
    for i, side in enumerate(stack[:n]):
        stack[i] = opposite(side)


def opposite(char):
    if char is '+':
        return '-'
    else:
        return '+'

main()
