filename = "A-large"
infile = filename+ ".in"
outfile = filename+ ".out"

f_in = open(infile, 'r')
f_out = open(outfile, 'w')

t = int(f_in.readline().strip())
print(t)
for case in range(0,t):
    num = int(f_in.readline().strip())
    res = "INSOMNIA"
    numseen = set()
    if num > 0:
        for j in range(1,1000000):
            numseen = numseen.union(set(str(j*num)))
            if len(numseen) == 10:
                res = j*num
                break;
    f_out.write("Case #{0}: {1}\n".format(case+1, res))