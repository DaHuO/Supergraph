d = {0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'}

from collections import Counter
import sys

def remove(digit, freq, c):
    for char in d[digit]:
        c[char] -= freq
        if c[char] == 0:
            del c[char]
    return c

filename = sys.argv[1]
with open(filename) as f:
    f.readline()
    i = 1
    for line in f:
        c = Counter(line.strip().lower())
        number = Counter()
        if 'z' in c:
            number[0] += c['z']
            c = remove(0, c['z'], c)
        if 'w' in c:
            number[2] += c['w']
            c = remove(2, c['w'], c)
        if 'u' in c:
            number[4] += c['u']
            c = remove(4, c['u'], c)
        if 'x' in c:
            number[6] += c['x']
            c = remove(6, c['x'], c)
        if 'g' in c:
            number[8] += c['g']
            c = remove(8, c['g'], c)
        if 'o' in c:
            number[1] += c['o']
            c = remove(1, c['o'], c)
        if 't' in c:
            number[3] += c['t']
            c = remove(3, c['t'], c)
        if 'f' in c:
            number[5] += c['f']
            c = remove(5, c['f'], c)
        if 's' in c:
            number[7] += c['s']
            c = remove(7, c['s'], c)
        number[9] += c['i']
        s = ''
        for n in sorted(number):
            s += str(n) * number[n]
        print 'Case #%d: %s' % (i, s)
        i += 1