
data = open("A-large.in").readlines()
tests = int(data[0])
data = data[1:]
answ = []

def calcsizes(n, g):
	if n == 0:
		a = [0, 0, 0]
		a[g] = 1
		return tuple(a)
	else:
		r1, p1, s1 = calcsizes(n-1, g)
		r2, p2, s2 = calcsizes(n-1, (g-1) % 3)
		return r1+r2, p1+p2, s1+s2

names = ['R', 'P', 'S']
def gentree(n, g):
	global names
	if n == 0:
		return names[g]
	else:
		p1 = gentree(n-1, g)
		p2 = gentree(n-1, (g-1) % 3)
		if p1 < p2:
			return p1 + p2
		else:
			return p2 + p1

for l in data:
	n, r, p, s = map(int, l.split(' '))
	pl = r, p, s
	if pl == calcsizes(n, 1):
		answ.append(gentree(n, 1))
	elif pl == calcsizes(n, 0):
		answ.append(gentree(n, 0))
	elif pl == calcsizes(n, 2):
		answ.append(gentree(n, 2))
	else:
		answ.append("IMPOSSIBLE")

with open("A-large.out", 'w') as f:
	for i,v in enumerate(answ):
		f.write("Case #{}: {}\n".format(i+1, v))
