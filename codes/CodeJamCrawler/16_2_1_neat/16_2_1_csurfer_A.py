from collections import defaultdict


def solve():
    nums = []
    freq = defaultdict(lambda: 0)
    for ch in list(raw_input()):
        freq[ch] += 1
    # ZERO
    for i in xrange(freq['Z']):
        nums.append(0)
    freq['E'] -= freq['Z']
    freq['R'] -= freq['Z']
    freq['O'] -= freq['Z']
    freq['Z'] = 0
    # TWO
    for i in xrange(freq['W']):
        nums.append(2)
    freq['T'] -= freq['W']
    freq['O'] -= freq['W']
    freq['W'] = 0
    # FOUR
    for i in xrange(freq['U']):
        nums.append(4)
    freq['F'] -= freq['U']
    freq['O'] -= freq['U']
    freq['R'] -= freq['U']
    freq['U'] = 0
    # SIX
    for i in xrange(freq['X']):
        nums.append(6)
    freq['S'] -= freq['X']
    freq['I'] -= freq['X']
    freq['X'] = 0
    # EIGHT
    for i in xrange(freq['G']):
        nums.append(8)
    freq['E'] -= freq['G']
    freq['I'] -= freq['G']
    freq['H'] -= freq['G']
    freq['T'] -= freq['G']
    freq['G'] = 0
    # ONE
    for i in xrange(freq['O']):
        nums.append(1)
    freq['N'] -= freq['O']
    freq['E'] -= freq['O']
    freq['O'] = 0
    # THREE
    for i in xrange(freq['H']):
        nums.append(3)
    freq['T'] -= freq['H']
    freq['R'] -= freq['H']
    freq['E'] -= freq['H']
    freq['E'] -= freq['H']
    freq['H'] = 0
    # FIVE
    for i in xrange(freq['F']):
        nums.append(5)
    freq['I'] -= freq['F']
    freq['V'] -= freq['F']
    freq['E'] -= freq['F']
    freq['F'] = 0
    # SEVEN
    for i in xrange(freq['S']):
        nums.append(7)
    freq['E'] -= freq['S']
    freq['V'] -= freq['S']
    freq['E'] -= freq['S']
    freq['N'] = 0
    # NINE
    for i in xrange(freq['E']):
        nums.append(9)
    return ''.join(map(str, sorted(nums)))

tc = int(input())
TC = int(tc)
while tc > 0:
    tc -= 1
    ans = solve()
    print 'Case #{}: {}'.format(TC - tc, ans)
