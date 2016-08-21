from __future__ import division
import sys
sys.setrecursionlimit(10000)
EXAMPLE_IN = """\
5
0
1
2
11
1692
"""

EXAMPLE_OUT = """\
Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
Case #5: 5076
"""

def solve(j):
    if j == 0:
        return 'INSOMNIA'
    seen = set()
    for i in range(1, 10000):
        num = str(i*j)
        seen.update(set(num))
        if len(seen) == 10:
            return str(num)
    else:
        return 'INSOMNIA'

def main(lines):
    for i in range(int(next(lines))):
        num = int(next(lines).strip())
        ans = 'Case #%d: %s' % (i+1, solve(num))
        print(ans)




if __name__ == '__main__':
    if len(sys.argv) == 1:
        input = iter(EXAMPLE_IN.split('\n'))
    else:
        input = open(sys.argv[1])
    main(input)
