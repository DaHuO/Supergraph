#!/usr/bin/python

import sys
import re

def main():
    fIn = sys.argv[1]

    with open(fIn, 'r') as f:
        T = int(f.readline())

        i = 0

        for t in range(T):
            cakes = f.readline().strip()
            correctCakes = ''.join(['+' for _ in range(len(cakes))])
            
            ans = 0
            while cakes != correctCakes:
                # print 'cakes: %s, correctCakes: %s' % (cakes, correctCakes)
                ans += 1
                
                m = re.match('^-*', cakes)
                minuses = len(m.group(0))
                if len(m.group(0))>0:
                    cakes = re.sub('^-*', ''.join(['+' for _ in range(minuses)]), cakes)
                else:
                    m = re.match('^\+*', cakes)
                    pluses = len(m.group(0))
                    cakes = re.sub('^\+*', ''.join(['-' for _ in range(pluses)]), cakes)

            print "Case #%d: %d" % ((t+1), ans)
			

if __name__ == '__main__':
    sys.exit(main())
