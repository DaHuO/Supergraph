import sys
dic ={}
dic["+"] = 0
dic["-"] = 1
dic["+-"] = 2
def solve(a):
	if a in dic:
		return dic[a]
	else:
		if a[-1] == "+":
			dic[a[:-1]] = solve(a[:-1])
			return dic[a[:-1]]
		else:
			c= len(a)
			b = (len(a)/2)
			l = list(a)
			if(a[0] == "+"):
				for s in range(1,c):
					if(a[s]!= "+"):
						break
				for i in range(s):
					l[i] = "-"
				q = ''.join(l)
				dic[q] = solve(q)
				return 1+dic[q]
			else:
				for i in range(len(a)):
					if(l[i] == "+"):
						l[i] = "-"
					else:
						l[i] = "+"
				for i in range(b):
					l[i],l[c-1-i] = l[c-i-1],l[i]

				p = ''.join(l)
				dic[p] = solve(p)
				return 1+dic[p] 

for t in range(input()):
	a = raw_input()
	print "Case ",
	sys.stdout.write("#"),
	print t+1,
	sys.stdout.write(":"),
	print "",solve(a)