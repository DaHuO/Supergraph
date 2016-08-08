T = int(raw_input())

def check(p,r,s):
	if (p+r+s) == 1:
		return True
	pairs = (p+r+s)/2
	pr = pairs-s
	ps = pairs-r
	rs = pairs-p
	if pr < 0 or ps < 0 or rs < 0:
		return False
	return check(pr,rs,ps)

def solve_pair(p):
	if p == "PR" or p == "RP":
		return "P"
	if p == "PS" or p == "SP":
		return "S"
	if p == "RS" or p == "SR":
		return "R"

def find_min(p,r,s,order):
	if (p+r+s) == 1:
		if p == 1:
			return "P"
		if r == 1:
			return "R"
		if s == 1:
			return "S"
	pairs = (p+r+s)/2
	pr = pairs-s
	ps = pairs-r
	rs = pairs-p
	new_ord = solve_pair(order[0]+order[1]) + solve_pair(order[0]+order[2]) + solve_pair(order[1]+order[2])
	s = find_min(pr,rs,ps,new_ord)
	ret = ""
	for c in s:
		if c == "P":
			if order.find("P") < order.find("R"):
				ret += "PR"
			else:
				ret += "RP"
		if c == "R":
			if order.find("R") < order.find("S"):
				ret += "RS"
			else:
				ret += "SR"
		if c == "S":
			if order.find("S") < order.find("P"):
				ret += "SP"
			else:
				ret += "PS"
	return ret
	
def solve():
	N,r,p,s = map(int,raw_input().split(' '))
	if check(p,r,s):
		return find_min(p,r,s,"PRS")
	else:
		return "IMPOSSIBLE"
	
for i in range(1,T+1):
	print "Case #" + str(i) + ": " + solve()
