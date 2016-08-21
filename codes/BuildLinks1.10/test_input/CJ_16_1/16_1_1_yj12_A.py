def solve(line):
    idx = [[0]]
    for i in range(1,len(line)):
	temp = [[jj for jj in j] for j in idx]
	for t in temp:
	    t.append(i)
	for j in idx:
	    j.insert(0,i)
	idx.extend(temp)
    
    A = []
    for i in idx:
	a = ''.join(line[ii] for ii in i)
	A.append(a)
    A.sort()
    return A[-1]

file = 'A-small-attempt0.in'
fileout = 'A-small-attempt0.out'
cases=[]
with open(file) as f:
    f.readline()
    for line in f.readlines():
	cases.append(line.strip())

f = open(fileout, 'w')
for i, c in enumerate(cases):
    print i
    soln = solve(c)
    f.write('Case #' + str(i+1) + ': ' + str(soln) + '\n')
f.close()