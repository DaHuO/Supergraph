import sys
'''
Getting the Digits
'''

if __name__ == '__main__':
    f = sys.stdin
    T = int(f.readline())
    index = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
    for x in xrange(1, T + 1):
        s = f.readline().strip()
        L = []
        a = [('Z', 'ZERO'), ('W', 'TWO'), ('U', 'FOUR'), ('X', 'SIX'), ('G', 'EIGHT'), ('O', 'ONE'), ('T', 'THREE'), ('F', 'FIVE'), ('S', 'SEVEN'), ('I', 'NINE')]
        for i, t in enumerate(a):
            while s.find(t[0]) != -1:
                L.append(index[i])
                for c in t[1]:
                    s = s.replace(c, '', 1)
        L.sort()
        print "Case #%d: %s" % (x, ''.join(map(str, L)))
