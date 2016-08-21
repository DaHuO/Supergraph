filename = "B-large"
infile = filename+ ".in"
outfile = filename+ ".out"

f_in = open(infile, 'r')
f_out = open(outfile, 'w')

t = int(f_in.readline().strip())
print(t)
for case in range(0,t):
    str = f_in.readline().strip()
    str = str[::-1]
    res = -1
    if str[0] == '-':
        res = 1
    else:
        res = 0
    for i in range(0,len(str)-1):
        if str[i] != str[i+1]:
            res += 1
    f_out.write("Case #{0}: {1}\n".format(case+1, res))