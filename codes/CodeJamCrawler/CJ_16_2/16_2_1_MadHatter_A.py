__author__ = 'dkopiychenko'

# g = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
#
# d = {}
# for i,x in enumerate(g):
#     for c in x:
#         if c in d:
#             d[c].append(i)
#         else: d[c] = [i]
# print d


def solve(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else: d[c] = 1

    dd = {}
    dd[8] = d['G'] if 'G' in d else 0
    dd[6] = d['X'] if 'X' in d else 0
    dd[4] = d['U'] if 'U' in d else 0
    dd[2] = d['W'] if 'W' in d else 0
    dd[0] = d['Z'] if 'Z' in d else 0
    dd[7] = (d['S']-dd[6]) if 'S' in d else 0
    dd[5] = (d['F']-dd[4]) if 'F' in d else 0
    dd[3] = (d['H']-dd[8]) if 'H' in d else 0
    dd[1] = (d['O']-dd[0]-dd[2]-dd[4]) if 'O' in d else 0
    dd[9] = (d['N']-dd[1]-dd[7])/2 if 'N' in d else 0

    r = []
    for k,v in dd.items():
        r += [k]*v
    r.sort()

    return ''.join(map(str,r))

t = int(raw_input())
for i in xrange(t):
    s = raw_input().strip()
    print 'Case #' + str(i+1) + ': ' + str(solve(s))
