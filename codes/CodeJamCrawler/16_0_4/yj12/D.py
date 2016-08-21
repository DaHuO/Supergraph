from math import ceil
#file = 'D-small-attempt0.in'
file = 'D-large.in'
#file = 'tile.in'
#fileout = 'tile.large.out'
fileout = 'D-large.out'

def findnode(positions, k, c):
    node = 0
    for i in range(c):
	size = k**(c-(i+1))
#	print 'k:', k, 'c:', c, 'i:', i, 'c-(i+1):', c-(i+1)
	node += size * positions[i]
#	print 'position:', positions[i], 'size:', size, 'node:', node
    return node

def solve(c):
    k, c, s = c
    req = int(ceil(float(k)/float(c)))
    if s < req:
	return 'IMPOSSIBLE'

#    print '------------------', k,c,s, 'req:', req
    soln = []
    for i in range(req):
	interval = range((i*c), (i+1)*c)
	interval = [ii if ii < k else k-1 for ii in interval ]
	#interval = [ii if ii < k else 0 for ii in interval ]
#	print interval
	soln.append(findnode(interval, k, c) + 1)
    return ' '.join(map(str, soln))

cases=[]
with open(file) as f:
    f.readline()
    for line in f.readlines():
	line.strip()
	cases.append(map(int, line.split(' ')))

f = open(fileout, 'w')
for i, c in enumerate(cases):
    #ans = range(1, c[0]+1)
    ans = solve(c)
#    print ans
    f.write('Case #' + str(i+1) + ': ' + ans + '\n')

f.close()