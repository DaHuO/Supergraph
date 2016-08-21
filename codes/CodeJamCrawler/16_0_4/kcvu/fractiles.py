#!/usr/bin/env python

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as infile:
        _ = infile.readline()
        line_index = 0
        for line in infile:
            k, _, _ = line.strip().split()
            k = int(k)
            line_index += 1
            print 'Case #%d: %s' % (line_index,' '.join([str(v) for v in range(1,k+1)]))

