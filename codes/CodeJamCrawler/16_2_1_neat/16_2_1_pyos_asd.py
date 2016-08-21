import sys
import collections


digits =  ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
stages = [['Z',     None, 'W',   None,    'U',    None,   'X',   None,    'G',     None  ],
          [None,    'O',  None,  'R',     None,   'F',    None,  'S',     None,    None  ],
          [None,    None, None,  None,    None,   None,   None,  None,    None,    'I'   ]]


def f(x):
    c = collections.Counter(x)
    r = [0] * 10
    for s in stages:
        for i, q in enumerate(s):
            if q:
                r[i] = n = c[q]
                for v in digits[i]:
                    c[v] -= n
    assert not any(c.values()), (x, r, c)
    return ''.join(str(i) * n for i, n in enumerate(r))


for i in range(int(sys.stdin.readline())):
    print('Case #{}: {}'.format(i + 1, f(sys.stdin.readline().strip())))
