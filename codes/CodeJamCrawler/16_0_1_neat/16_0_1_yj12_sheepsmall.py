from math import log10
from math import pow
#file = 'sheep.in'
#file = 'A-small-attempt0.in'
file = 'A-large.in'
def solve(t):
    seen = [False] * 10
    for i in range(1, 100):
	tt = t * i
	stt = str(tt)
	for s in stt:
	    seen[int(s)] = True
	    if all(seen):
		return str(tt)

with open(file) as f:
    f.readline()
    T = map(int, f.readlines())

f = open('sheep.out', 'w')
for i, t in enumerate(T):
#    for i in range(100):
#	print t * i
    if t == 0:
	ans = 'INSOMNIA'
    else:
	ans = solve(t)
    f.write('Case #' + str(i+1) + ': ' + ans + '\n')
    print 'Case #' + str(i+1) + ':', t, ans
#    dig = int(log10(tt) + 1)
#    print tt, dig