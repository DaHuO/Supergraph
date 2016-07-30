from math import sqrt
from scipy.misc import comb #use comb(n,k,True)

NN = 12

def expand(c):
    if c == 'P':
        return 'PR'
    if c == 'R':
        return 'RS'
    if c == 'S':
        return 'PS'

def alphexpand(line):
    if len(line) == 1:
        return expand(line[0])
    else:
        mid = len(line)/2
        a = alphexpand(line[:mid])
        b = alphexpand(line[mid:])
        return ''.join([min(a,b), max(a,b)])
                 
dic = {}

def build(s, dic):
    #s = 'P', 'R', 'S'
    line = s
    for i in xrange(NN):
        line = alphexpand(line)
        p = line.count('P')
        r = line.count('R')
        s = line.count('S')
        
        dic[(i+1, r, p, s)] = line
        #print line
    return line

for x in ('P', 'R', 'S'):
    build(x,dic)
    
def Next(N,R,P,S, dic):
    return dic.get((N, R, P, S), 'IMPOSSIBLE')
        

#input = open(r'sample.in')
#input = open(r'A-small-attempt1.in')
input = open(r'A-large.in')

T = int(input.readline())

sol = []

for i in xrange(T):
    N,R,P,S = (int(x) for x in input.readline().strip().split())
    sol += [Next(N, R,P,S, dic)]
    if not i%10: print i


tofile = True
if tofile:
    with open(r'./outputA-L.txt', 'w') as output:
        for i in range(len(sol)):
            output.write('Case #%s: %s\n' % (i+1, sol[i]))
else:
    print sol


