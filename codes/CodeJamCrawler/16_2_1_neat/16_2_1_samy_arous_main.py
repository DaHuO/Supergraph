import collections

def solve(s):
    number = [
        "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
    ]
    counts = [0] * 10

    c = collections.Counter(s)
    if c.get('Z', 0) > 0:
        counts[0] += c.get('Z')
        # number contains 0
        for ch in 'ZERO':
            c[ch] -= counts[0]
    if c.get('W', 0) > 0:
        counts[2] += c.get('W')
        # number contains 0
        for ch in 'TWO':
            c[ch] -= counts[2]
    if c.get('U', 0) > 0:
        counts[4] += c.get('U')
        # number contains 0
        for ch in 'FOUR':
            c[ch] -= counts[4]
    if c.get('X', 0) > 0:
        counts[6] += c.get('X')
        # number contains 0
        for ch in 'SIX':
            c[ch] -= counts[6]
    if c.get('G', 0) > 0:
        counts[8] += c.get('G')
        # number contains 0
        for ch in 'EIGHT':
            c[ch] -= counts[8]

    if c.get('F', 0) > 0:
        counts[5] += c.get('F')
        # number contains 0
        for ch in 'FIVE':
            c[ch] -= counts[5]
    if c.get('H', 0) > 0:
        counts[3] += c.get('H')
        # number contains 0
        for ch in 'THREE':
            c[ch] -= counts[3]
    if c.get('S', 0) > 0:
        counts[7] += c.get('S')
        # number contains 0
        for ch in 'SEVEN':
            c[ch] -= counts[7]
    if c.get('I', 0) > 0:
        counts[9] += c.get('I')
        # number contains 0
        for ch in 'NINE':
            c[ch] -= counts[9]
    if c.get('O', 0) > 0:
        counts[1] += c.get('O')
        # number contains 0
        for ch in 'ONE':
            c[ch] -= counts[1]

    res = ''.join([str(i) * c for i, c in enumerate(counts)])
    return res,




def read_input():
    return raw_input(),

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        res = map(str, solve(*read_input()))
        print "Case #%s: %s" % ( i+1, " ".join(res) )

    # test_cases = [
    #     ( 'OZONETOWER', ),
    #     ( 'WEIGHFOXTOURIST', ),
    #     ( 'OURNEONFOE', ),
    #     ( 'ETHER', ),
    # ]
    # for i, test in enumerate(test_cases):
    #     res = map(str, solve(*test))
    #     print "Case #%s: %s" % ( i+1, " ".join(res) )