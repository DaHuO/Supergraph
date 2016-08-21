from collections import defaultdict

T = int(raw_input().strip())

teleMap = {
    'ZERO': 0,  # number of Z
    'ONE': 1,  # remove 0, 2, 4, then number of O
    'TWO': 2,  # number of W
    'THREE': 3,  # remove 0,4 then number of R
    'FOUR': 4,  # number of U
    'FIVE': 5,  # remove 7, then number of V
    'SIX': 6,  # number of X
    'SEVEN': 7,  # remove 6, then number of S
    'EIGHT': 8,  # number of G
    'NINE': 9,  # remove 5, 6, 8 then number of I
}
codes = sorted(teleMap.keys(), key=lambda x: len(list(x)), reverse=True)

"""
teleMap = {
    'ZERO': 0,  # number of Z
    'TWO': 2,  # number of W
    'FOUR': 4,  # number of U
    'SIX': 6,  # number of X
    'EIGHT': 8,  # number of G
    'ONE': 1,  # remove 0, 2, 4, then number of O
    'THREE': 3,  # remove 0,4 then number of R
    'SEVEN': 7,  # remove 6, then number of S
    'FIVE': 5,  # remove 7, then number of V
    'NINE': 9,  # remove 5, 6, 8 then number of I
}
"""


def countCharacter(S):
    ret = defaultdict(int)
    for c in S:
        ret[c] += 1
    return ret


for t in xrange(T):
    S = raw_input().strip()
    listS = list(S)

    ans = []

    counts = countCharacter(S)

    ans = ans + ['ZERO'] * counts['Z']
    ans = ans + ['TWO'] * counts['W']
    ans = ans + ['FOUR'] * counts['U']
    ans = ans + ['SIX'] * counts['X']
    ans = ans + ['EIGHT'] * counts['G']

    for code in ans:
        for c in code:
            counts[c] -= 1

    _ans = []
    _ans = _ans + ['ONE'] * counts['O']
    _ans = _ans + ['THREE'] * counts['R']
    _ans = _ans + ['SEVEN'] * counts['S']

    for code in _ans:
        for c in code:
            counts[c] -= 1
    ans = ans + _ans

    _ans = []
    _ans = _ans + ['FIVE'] * counts['V']
    for code in _ans:
        for c in code:
            counts[c] -= 1
    ans = ans + _ans

    _ans = []
    _ans = _ans + ['NINE'] * counts['I']
    ans = ans + _ans

    # assert len(listS) == 0, listS
    ans = ''.join(sorted(map(lambda x: str(teleMap[x]), ans)))

    print 'Case #%d: %s' % (t + 1, ans)
