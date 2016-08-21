from collections import defaultdict

def solve(s):
    d = defaultdict(int)
    for ch in s:
        d[ch] += 1
    ans = ''

    count = d['Z']
    ans += '0'*count
    d['E'] -= count
    d['R'] -= count
    d['O'] -= count

    count = d['O'] - d['W'] - d['U']
    ans += '1'*count
    d['O'] -= count
    d['N'] -= count
    d['E'] -= count

    count = d['W']
    ans += '2'*count
    d['T'] -= count
    d['O'] -= count

    count = d['T'] - d['G']
    ans += '3'*count
    for l in 'THREE': d[l] -= count

    count = d['U']
    ans += '4'*count
    for l in 'FOR': d[l] -= count

    count = d['F']
    ans += '5'*count
    for l in 'IVE': d[l] -= count

    count = d['X']
    ans += '6'*count
    for l in 'SI': d[l] -= count

    count = d['V']
    ans += '7'*count
    for l in 'SEEN': d[l] -= count

    count = d['G']
    ans += '8'*count
    for l in 'EIHT': d[l] -= count

    ans += '9'*d['I']
    check(s, ans)
    return ans

def check(s, n):
    d = defaultdict(int)
    for ch in s: d[ch] += 1
    s2 = ''.join(map(('ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE').__getitem__, map(int, n)))
    d2 = defaultdict(int)
    for ch in s2: d2[ch] += 1
    assert d == d2, (s, n)

for i in range(int(input())):
    print("Case #", i+1, ": ", solve(input()), sep='')

