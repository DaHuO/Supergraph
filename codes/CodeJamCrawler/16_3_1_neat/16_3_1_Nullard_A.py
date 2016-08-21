import sys
import os
import glob

input_file = None
def readone(t): return t(input_file.readline().strip())
def readmany(t): return map(t, input_file.readline().split())


def ltr(x):
    return chr(ord('A') + x)

def solve():
    n = readone(int)
    p = readmany(int)
    cp = list(p)
    sp = sorted(p, reverse=True)
    order = []
    for i in range(n):
        ind = cp.index(sp[i])
        order.append(ind)
        cp[ind] = -1
    evac = []
    total = sum(p)
    gone = 0
    last = 0
    print p
    print order
    lastnum = 1000
    while gone < total:
        if total - gone == 2:
            ltrs = []
            for i in range(n):
                if p[order[i]] > 0:
                    ltrs.append(ltr(order[i]))
            evac.append(''.join(ltrs))
            break
        elif total - gone == 3:
            for i in range(n):
                if p[order[i]] > 0:
                    evac.append(ltr(order[i]))
                    gone += 1
                    p[order[i]] -= 1
                    break
        elif p[order[last]] != lastnum:
            last = 0
            lastnum = p[order[0]]
            continue
        elif last == n - 1:
            evac.append(ltr(order[last]))
            gone += 1
            p[order[last]] -= 1
            last = 0
        elif p[order[last]] == p[order[last + 1]]:
            evac.append(ltr(order[last]) + ltr(order[last + 1]))
            gone += 2
            p[order[last]] -= 1
            p[order[last + 1]] -= 1
            if last + 2 == n:
                last = 0
            else:
                last += 2
        elif p[order[last]] > p[order[last + 1]]:
            evac.append(ltr(order[last]))
            gone += 1
            p[order[last]] -= 1
            last = 0
    return ' '.join(evac)
            
if __name__ == '__main__':
    input_file = sys.stdin
    problem = os.path.split(__file__)[1][0].upper()
    output_filename = 'test.out'
    inputs = glob.glob(os.path.expanduser('~') + '/Downloads/' + problem + '-*.in')
    newest = max(inputs, key=os.path.getctime)
    input_filename = os.path.split(newest)[1]
    output_filename = problem + '-' + input_filename.split('-')[1][:-3] + '.out'
    input_file = open(newest)
    T = int(input_file.readline().strip())
    output_file = open(output_filename, 'w')
    for t in xrange(T):
        result = solve()
        output_file.write("Case #%d: %s\n" % (t + 1, result))
        print "Case #%d: %s" % (t + 1, result)
    