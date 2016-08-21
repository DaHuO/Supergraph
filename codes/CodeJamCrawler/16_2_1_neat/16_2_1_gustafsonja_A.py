import fileinput

digits = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

letters = set()
for d in digits:
    for c in d:
        letters.add(c)

def mult(s):
    m = {}
    for l in letters:
        m[l] = 0
    for c in s:
        m[c] += 1
    return m

dmult = {d: mult(digits[d]) for d in range(10)}

def has(m1, m2):
    return all([m1[l] >= m2[l] for l in letters])

def n(m, min=0):
    for i in range(min, 10):
        if has(m, dmult[i]):
            newm = {l: m[l] - dmult[i][l] for l in letters}
            if all([newm[l] == 0 for l in letters]):
                return str(i)
            rest = n(newm, i)
            if rest:
                return str(i) + rest
    return None

f = fileinput.input()
T = int(f.readline())
for t in range(1, T+1):
    s = f.readline().strip()
    m = mult(s)
    number = n(m)
    print('Case #{0}: {1}'.format(t, number))
