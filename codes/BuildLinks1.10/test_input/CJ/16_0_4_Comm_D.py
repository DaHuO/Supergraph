import numpy as np
  

def output(i, out):
    with open('D-small.out', 'a') as outfile:
        outfile.write("Case #{0}: {1}\n".format(i, out))

def solve(i, line):
    sline = line.split(' ')
    K = int(sline[0])
    C = int(sline[1])
    S = int(sline[2])
    if S == K:
    
        out = ' '.join([str(x+1) for x in range(S)])
    else:
        out = "IMPOSSIBLE"
    output(i, out)
    

lines = open('D-small-attempt0.in').readlines()

for i, line in enumerate(lines):
    if i > 0:
        solve(i, line)