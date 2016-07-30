#!/usr/bin/python3

from codejam import CodeJam

def docase(f):
    (n, r, p, s) = (int(_) for _ in f.readline().split())
    if max(abs(r-p), abs(r-s), abs(p-s)) != 1:
        return 'IMPOSSIBLE'
    nm = n % 6
    beats = {'P' : 'R', 'R' : 'S', 'S' : 'P'}
    if r == s:
        if p > r:
            if nm == 2:
                b = 'P'
                c = 'R'
                a = 'S'
            elif nm == 4:
                c = 'P'
                a = 'R'
                b = 'S'
            elif nm == 6:
                a = 'P'
                b = 'R'
                c = 'S'
            else:
                return 'IMPOSSIBLE'
        else:
            if nm == 1:
                c = 'P'
                a = 'R'
                b = 'S'
            elif nm == 3:
                a = 'P'
                b = 'R'
                c = 'S'
            elif nm == 5:
                b = 'P'
                c = 'R'
                a = 'S'
            else:
                return 'IMPOSSIBLE'
    if p == s:
        if r > p:
            if nm == 2:
                b = 'R'
                a = 'P'
                c = 'S'
            elif nm == 4:
                c = 'R'
                b = 'P'
                a = 'S'
            elif nm == 6:
                a = 'R'
                c = 'P'
                b = 'S'
            else:
                return 'IMPOSSIBLE'
        else:
            if nm == 1:
                c = 'R'
                b = 'P'
                a = 'S'
            elif nm == 3:
                a = 'R'
                c = 'P'
                b = 'S'
            elif nm == 5:
                b = 'R'
                a = 'P'
                c = 'S'
            else:
                return 'IMPOSSIBLE'
    if r == p:
        if s > r:
            if nm == 2:
                b = 'S'
                c = 'P'
                a = 'R'
            elif nm == 4:
                c = 'S'
                a = 'P'
                b = 'R'
            elif nm == 6:
                a = 'S'
                b = 'P'
                c = 'R'
            else:
                return 'IMPOSSIBLE'
        else:
            if nm == 1:
                c = 'S'
                a = 'P'
                b = 'R'
            elif nm == 3:
                a = 'S'
                b = 'P'
                c = 'R'
            elif nm == 5:
                b = 'S'
                c = 'P'
                a = 'R'
            else:
                return 'IMPOSSIBLE'

    def expand(a, r):
        if r == 0:
            return a
        x = expand(a, r-1)
        y = expand(beats[a], r-1)
        return ''.join(sorted((x, y)))
    return expand(a, n)
    #field = a
    #for round in range(n):
    #    newfield = ''
    #    for ct in field:
    #        newfield += ''.join(sorted(ct + beats[ct]))
    #    field = newfield
    #return field


cj = CodeJam(docase)

# After importing cj into an interactive terminal, I test the code by
# running:
# >>> cj.processtext("""examples""")
#
# Then after downloading the problem set, I solve it with:
# >>> cj.processfile('filename')
