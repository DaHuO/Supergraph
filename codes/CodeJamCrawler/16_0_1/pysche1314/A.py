
infile = 'A.in'
outfile = 'A.out'
cases = 0
test = 0
outf = open(outfile, 'w')

with open(infile) as f:
    t = 0
    for line in f:
        if t == 0:
            cases = int(line)
            t += 1
            continue
        else:
            num = int(line)
        if num == 0:
            outf.write("Case #%s: INSOMNIA\n" % t)
        else:
            mark = {}
            idx = 1
            cur = num
            while True:
                test = cur
                while test > 0:
                    m = test % 10
                    mark[m] = 1
                    test /= 10
                if len(mark) == 10:
                    break
                idx += 1
                cur = num * idx
            outf.write("Case #%s: %s\n" % (t, cur))
        
        print t
        if t == cases:
            break
        t += 1
outf.close()