
import sys

data = "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" 

def update(cmap, s, n):
    for c in s:
        if c in s:
            cmap[c] -= n

def solve(s):
    count = [0] * 10
    cmap = {}
    for c in s:
        cmap[c] = cmap.get(c, 0) + 1
    if cmap.get('Z'):
        count[0] = cmap['Z']
        update(cmap, data[0], count[0])
    if cmap.get('W'):
        count[2] = cmap['W']
        update(cmap, data[2], count[2])
    if cmap.get('U'):
        count[4] = cmap['U']
        update(cmap, data[4], count[4])
    if cmap.get('X'):
        count[6] = cmap['X']
        update(cmap, data[6], count[6])
    if cmap.get('G'):
        count[8] = cmap['G']
        update(cmap, data[8], count[8])
    if cmap.get('R'):
        count[3] = cmap['R']
        update(cmap, data[3], count[3])
    if cmap.get('O'):
        count[1] = cmap['O']
        update(cmap, data[1], count[1])
    if cmap.get('S'):
        count[7] = cmap['S']
        update(cmap, data[7], count[7])
    if cmap.get('F'):
        count[5] = cmap['F']
        update(cmap, data[5], count[5])
    if cmap.get('I'):
        count[9] = cmap['I']
        update(cmap, data[9], count[9])
    result = ''
    for k, v in enumerate(count):
        if v:
            result += ''.join([str(k)] * v)
    return result


def main():
    T = int(sys.stdin.readline())
    for i in xrange(T):
        s = sys.stdin.readline().strip()
        print "Case #%d: %s" % (i + 1, solve(s))


if __name__ == '__main__':
    main()
