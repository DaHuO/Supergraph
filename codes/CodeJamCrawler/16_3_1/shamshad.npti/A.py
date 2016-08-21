
T = int(raw_input())

for t in range(1, T + 1):
	n = int(raw_input())
	p = map(int, raw_input().split())
	a = []
	y = ord('A')
	a = [[p[i], chr(y + i)] for i in range(len(p))]
	out = []
	a.sort()
	while a[-1][0] != 0:
		if a[-1][0] <= 2:
			z = 0
			y = 0
			for i in range(len(p)):
				if a[i][0] == 1:
					y = i
					z+=1
			if z % 2 == 1:
				if y == len(p) - 1:				
					out.append(a[y][1])
					a[y][0] -= 1
				else:
					out.append(a[-1][1])
					a[-1][0] -= 1
			else:
				if a[-1][0] == a[-2][0]:
					out.append(a[-1][1] + a[-2][1])
					a[-1][0] -= 1
					a[-2][0] -= 1
				else:
					out.append(a[-1][1]+a[-1][1])
					a[-1][0] -= 2
		elif a[-1][0] >= a[-2][0] + 2:
			out.append(a[-1][1] + a[-1][1])
			a[-1][0] -= 2
		else:
			out.append(a[-1][1] + a[-2][1])
			a[-1][0] -= 1
			a[-2][0] -= 1
		a.sort()
	print "Case #%d: %s" % (t, ' '.join(out))