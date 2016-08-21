import sys
savein = sys.stdin
saveout = sys.stdout

fin = open('A-large.in','r')
fout = open('A-large.out','w')

sys.stdin = fin
sys.stdout = fout

t = int(input())

for x in range(0,t):
	a = set()
	n = int(input())
	if n == 0:
		print("Case #{0}: INSOMNIA".format(x+1))
	else:
		i = 1

		while len(a) < 10:
			m = str(i*n)
			i+=1
			for y in m:
				a.add(y)
		print("Case #{0}: {1}".format(x+1, m))

sys.stdin = savein
sys.stdou = saveout
fin.close()
fout.close()
