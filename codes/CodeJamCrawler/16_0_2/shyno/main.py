'''
Revenge of the Pancakes
'''

if __name__ == '__main__':
    f = open("B-large.in")
    nc = int(f.readline())
    for x in xrange(1, nc+1):
        s = f.readline().rstrip("+\n")
        m = 0
        while s:
            i = 0
            while s[i] == '+':
                i += 1
            s = s.replace('+', '-', i)
            if i:
                m += 1
            s = s[::-1]
            ss = ''
            for c in s:
                if c == '+':
                    ss += '-'
                else:
                    ss += '+'
            s = ss
            m += 1
            s = s.rstrip('+')
        print "Case #%d: %d" % (x, m)
