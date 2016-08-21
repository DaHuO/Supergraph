f = open('input.in')
rows = []
for row in f:
    row = row.strip()
    rows.append(row)


def flip(p):
    z = 1
    o = []
    for q in range(0, len(p) - 1):
        if p[q] == p[q+1]:
            z += 1
        else:
            break
    for q in range(0, z):
        if p[q] == '+':
            o.append('-')
        else:
            o.append('+')
    return ''.join(o) + p[z:]


def is_happy(p):
    for q in range(0, len(p)):
        if p[q] == '-':
            return False
    return True

n = int(rows[0])
c = 1
for i in range(1, n + 1):
    flips = 0
    pancakes = rows[i]
    while not is_happy(pancakes):
        pancakes = flip(pancakes)
        flips += 1
    print "Case #{0}: {1}".format(c, flips)
    c += 1

