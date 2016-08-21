import numpy as np

def output(i, out):
    with open('A-large.out', 'a') as outfile:
        outfile.write("Case #{0}: {1}\n".format(i, out))

def solve(i, n):
    fullarr = set(str(x) for x in range(10))
    constarr = set()
    m = n
    if m == 0:
        out = "INSOMNIA"
        output(i, out)
    else:
        while (fullarr != constarr):
            nums = set(str(m))
            constarr = nums.union(constarr)
            if constarr == fullarr:
                out = str(m)
                output(i, out)
            else:
                m += n
                
    

lines = np.loadtxt('A-large.in', dtype=int)

for i, line in enumerate(lines):
    if i > 0:
        solve(i, line)