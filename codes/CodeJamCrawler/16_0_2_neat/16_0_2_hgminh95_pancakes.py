from sys import argv

_, infile, outfile = argv

out = open(outfile, 'w')

with open(infile) as f:
    n = int(f.readline())
    
    for t in xrange(n):
        a = f.readline()[:-1]
        l = len(a)

        res = [[0 for x in xrange(2)] for x in xrange(l)]
        if (a[0] == '-'):
            res[0][0] = 0
            res[0][1] = 1
        else:
            res[0][0] = 1
            res[0][1] = 0

        for i in xrange(1, l):
            for j in xrange(2):
                if (j == 0 and a[i] == '-'):
                    res[i][j] = res[i - 1][j]
                    continue
                if (j == 1 and a[i] == '+'):
                    res[i][j] = res[i - 1][j]
                    continue
                
                res[i][j] = 1 + res[i - 1][1 - j]
        
        out.write("Case #{0}: {1}".format(t + 1, res[l - 1][1]))
        out.write("\n")

    out.close()                           

