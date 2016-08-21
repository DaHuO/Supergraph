#!/usr/bin/python

import sys


if __name__ == '__main__':

    fname = sys.argv[-1]
    with open(fname, 'r') as f:
        lines = [l[:-1] for l in f.readlines()]

    outlines = []

    digits = {
            'ZERO': 0,
            'ONE': 1,
            'TWO': 2,
            'THREE': 3,
            'FOUR': 4,
            'FIVE': 5,
            'SIX': 6,
            'SEVEN': 7,
            'EIGHT': 8,
            'NINE': 9,
            }

    digits_sorted = [
            'ZERO',
            'ONE',
            'TWO',
            'THREE',
            'FOUR',
            'FIVE',
            'SIX',
            'SEVEN',
            'EIGHT',
            'NINE',
            ]

    def contained(linea, d):
        for c in d:
            if linea.count(c) < d.count(c):
                return False
        return True

    for i, line in enumerate(lines[1:]):
        #
        blocked = []
        linea = '0'
        while len(linea):
            out = ''
            linea = [c for c in line]
            for d in digits_sorted:
                while contained(linea, d):
                    out_pot = out + ('%s' % digits[d])
                    if not out_pot in blocked:
                        out = out_pot
                        for c in d:
                            linea.remove(c)
                    else:
                        break
            blocked.append(out)
        #
        outlines.append('Case #%s: %s' % (i + 1, out))
        print out
        print linea
        assert(len(linea) == 0)

    fname = fname[:-2] + 'out'
    with open(fname, 'w') as f:
        outstr = '\n'.join(outlines)
        print outstr
        f.write(outstr)

