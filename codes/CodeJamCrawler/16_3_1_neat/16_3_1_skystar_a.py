f = open("D:\python\input.txt",'r')
t = int(f.readline())
#65 = A
m = 0
k = 0
s = 0
res = ''
allres = ''

for i in range(t):
	n = int(f.readline())
	p = list(int(x) for x in f.readline().split(' '))
	while True:
		if p.count(p[0]) == 2 and n == 2:
			res += "AB " * p[0]
			s = 1
			break
		for j in range(n):
			if p[j] > m:
				m = p[j]
				k = j
				
		res += chr(65+k) + ' '
		p[k] -= 1
		m = 0
		k = 0
		if p.count(0) == n: break
	res = res.strip()
	if s != 1:
		res = res[:len(res)-2] + res[-1]
	s = 0
	res = 'Case #%d: ' % (i+1) + res
	allres = allres + '\n' + res
	res = ''

f.close()

f = open("D:\python\output.txt","w")
f.write(allres)
f.close()