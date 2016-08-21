filename = "D-small-attempt0"
infile = filename+ ".in"
outfile = filename+ ".out"

f_in = open(infile, 'r')
f_out = open(outfile, 'w')

t = int(f_in.readline().strip())
print(t)
for case in range(0,t):
    line = f_in.readline().strip()
    k = int(line.split()[0])
    c = int(line.split()[1])
    print(k,c)
    res = [1]
    for i in range(0,k-1):
        res.append(res[-1] + k**(c-1))
    print(res)
    f_out.write("Case #{0}: {1}\n".format(case+1, ' '.join(map(lambda x: str(x),res))))