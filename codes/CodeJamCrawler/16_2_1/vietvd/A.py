ifile = open('A-large.in', 'r')
ofile = open('A-large.out', 'w')

TC = int(ifile.readline())

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

dat = [
    ['Z', '0'],
    ['X', '6'],
    ['W', '2'],
    ['G', '8'],
    ['U', '4'],
    ['R', '3'],
    ['S', '7'],
    ['V', '5'],
    ['O', '1'],
    ['I', '9']
]

def rem(S, w):
    for c in w:
        S.remove(c)
    return S

for tc in range(1, TC+1, 1):
    S = list(ifile.readline())

    ans = []
    for c,n in dat:
        if c in S:
            for i in xrange(S.count(c)):
                ans.append(n)
                S = rem(S, digits[int(n)])

    ans.sort()

    ofile.write("Case #{0}: {1}\n".format(tc, ''.join(ans)))
