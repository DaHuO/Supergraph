# -*- coding: utf-8 -*-

import sys

def check(seen):
    done = True
    for i in seen:
        if not seen[i] > 0:
            done = False
            break
    return done

def main():
    f = open(sys.argv[1])
    ncase = int(f.readline())
    for i in range(ncase):
        n = int(f.readline())
        # TODO
        seen = {}
        for j in range(10):
            seen[j] = 0
        if n == 0:
            print "Case #%d: INSOMNIA" % (i+1)
            continue
        ns = n + 0
        while True:
            nstr = "%d" % (ns)
            for char in nstr:
                seen[int(char)] = 1
            #print ns,n,seen
            if check(seen):
                print "Case #%d: %d" % (i+1,ns)
                break
            else:
                ns = ns + n
        #print i,ns


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
