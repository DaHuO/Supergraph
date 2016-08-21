import sys


class Prob1(object):
    def __init__(self, s):
        # reduce all strings
        l = list(reversed(list(s)))
        if '-' in l:
            self.s = l[l.index('-'):]
        else:
            self.s = []

    def toggle(self):
        if self.mark == '+':
            self.mark = '-'
        else:
            self.mark = '+'

    def solve(self):
        changes, index = 0,0
        self.mark = '+'
        while len(self.s) > 0:
            try:
                index = self.s.index(self.mark)
            except ValueError:
                if self.s[0] != self.mark:
                    changes += 1
                break
            self.s = self.s[index:]
            changes += 1
            self.toggle()
        return changes

output = "Case #%d: %s"

with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    for counter in xrange(T):
        data = f.readline().strip()
        s = [j for j in data]
        p1 = Prob1(s)
        print output % (counter+1, p1.solve())
