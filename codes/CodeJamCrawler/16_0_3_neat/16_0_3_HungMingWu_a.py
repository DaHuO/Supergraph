N = 16
J = 50
sols = []
divss = []
COUNT = 0
def calc(str, base):
	ret = 0
	for c in str:
		ret = ret * base + int(c)
	return ret;
def findDiv(v):
	div = 2;
	while True:
		if (div * div >v):
			break
		if (v % div == 0):
			return div
		div = div + 1
	return -1;
def DFS(depth, cur):
	if depth >= N:
		base = 2
		divs = []
		while True:
			if (base >= 11):
				break
			realValue = calc(cur, base)
			divs.append(findDiv(realValue))
			base = base + 1
		if -1 not in divs:
			temp = cur
			for div in divs:
				temp += ' ' + str(div)
			sols.append(temp)
		return
	if len(sols) == J:
		return
	if depth == 0:
		DFS(depth + 1, cur + '1')
	elif depth == N - 1:
		DFS(depth + 1, cur + '1')
	else:
		DFS(depth + 1, cur + '0')
		if len(sols) == J:
			return
		DFS(depth + 1, cur + '1')

T = int(raw_input(''))
N = int(raw_input(''))
J = int(raw_input(''))
DFS(0, '')
print "Case #1:"
for sol in sols:
	print sol
