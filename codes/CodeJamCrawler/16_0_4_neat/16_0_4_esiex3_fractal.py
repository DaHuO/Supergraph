__author__ = 'gosu'

from math import log

def main():
    inp = open("input.in")
    out = open('fractalout.txt', 'w')
    count = int(inp.readline())
    casenum = 1
    for x in range(count):
        linestr = inp.readline().strip()
        line = [int(a) for a in linestr.split()]
        k = line[0]
        c = line[1]
        s = line[2]
        solution = [str(a) for a in range(1, s + 1)]
        #print('Case #{0}: {1}'.format(casenum, ' '.join(solution)))
        out.write('Case #{0}: {1}'.format(casenum, ' '.join(solution)))
        out.write('\n')
        casenum += 1
    out.close()

if __name__ == '__main__':
    main()