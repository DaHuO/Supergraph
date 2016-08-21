filename = 'A-small-attempt1.in'
f = open(filename,'r')
T = int(f.readline())

def next(a,b,c):
	return a+b,b+c,a+c

def prev(a,b,c):
	return (a+c-b)/2 , (a+b-c)/2 , (-a+b+c)/2

x,y,z = 1,0,0


for i in range(1,T+1):
	print "Case #%d:" % i,
	n,r,p,s = map(int,f.readline().split())
	if max(r,p,s) - min(r,p,s) != 1:
		print "IMPOSSIBLE"
	else:
		a,b,c = r,p,s
		while sum([a,b,c]) != 1:
			a,b,c = prev(a,b,c)
		w = "RPS"
		a = w[[a,b,c].index(1)]
		
		"""
		for i in range(n):
			b = ""
			for j in a:
				if j == 'R':
					b += "SR"
				elif j == 'P':
					b += "PR"
				else:
					b += "PS"
			a = b[:]
		"""
		ans = dict()
		ans["P"] = ["P","PR","PRRS","PRRSPSRS"]
		ans["R"] = ["R","RS","PSRS","PRPSPSRS"]
		ans["S"] = ["S","PS","PRPS","PRPSPRRS"]

		print(ans[a][n])
