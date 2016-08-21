from sys import argv
from collections import Counter

validdigs = [
Counter('ZERO'),
Counter('ONE'),
Counter('TWO'),
Counter('THREE'),
Counter('FOUR'),
Counter('FIVE'),
Counter('SIX'),
Counter('SEVEN'),
Counter('EIGHT'),
Counter('NINE'),
]

def has(sup, sub):
    for l, f in sub.items():
        if sup[l] < f:
            return False
    return True

def get_digits(letters, digs):
    for i,d in enumerate(validdigs):
        if has(letters, d):
            newletters = letters-d
            newdigs = digs + [i]
            if len(newletters.most_common(1)):
                newdigs = get_digits(newletters, newdigs)
                if newdigs:
                    return newdigs
            else:
                return newdigs
    return None


if __name__ == '__main__':
    fin = open(argv[1], 'r')
    fout = argv[1] + '_out'

    with open(fout, 'w') as f:
        tnum = fin.readline()
        for i, l in enumerate(fin, 1):
            digs = get_digits(Counter(l.strip()), list())
            digs = sorted(digs)
            f.write('Case #{:}: {:}\n'.format(i,''.join(map(str,digs))))
