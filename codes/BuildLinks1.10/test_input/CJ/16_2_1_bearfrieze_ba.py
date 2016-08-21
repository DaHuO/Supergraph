T = int(input())

ns = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
os = [0, 2, 4, 6, 8, 7, 5, 3, 1, 9]

def containsNumber(s, number):
    tmp = s
    for c in number:
        if c in tmp:
            tmp = tmp.replace(c, '', 1)
        else:
            return (s, False)
    return [tmp, True]

def solve(s):
    digits = []
    while len(s):
        for i in os:
            s, res = containsNumber(s, ns[i])
            if res: digits.append(str(i))
    return ''.join(sorted(digits))

for case in range(1, T + 1):
    print('Case #%d: %s' % (case, solve(input())))
