f = open("test.in", "r")
new_file = open("testingOutput", "w")
t = int(f.readline())


def good_start (n,r,p,s):
	if n == 1:
		if p == 1 and r == 1:
			return "PR"
		if p == 1 and s == 1:
			return "PS"
		if r == 1 and s == 1:
			return "RS"
		else:
			return "IMPOSSIBLE"
	if r == 0 or p == 0 or s == 0:
		return "IMPOSSIBLE"
	total_amount = 2**n
	if r > total_amount/2 or p > total_amount/2 or s > total_amount/2:
		return "IMPOSSIBLE"
	if abs(r-p)>1 or abs(p-s) > 1 or abs(r-s)>1:
		return "IMPOSSIBLE"
	else:
		a= "PRPS"
		b= "PRRS"
		c= "PSRS"
		result = []
		if p>s and p>r:
			for i in range(0,p/4):
				result.append(a)
				result.append(b)
				result.append(c)
			result.append(a)
			return "".join(result)
		if r>s and r>p:
			for i in range(0,r/4):
				result.append(a)
				result.append(b)
				result.append(c)
			result.append(b)
			return "".join(result)
		if s>r and s>p:
			if n == 2:
				return c
			for i in range(1,s/4):
				result.append(a)
				result.append(b)
				result.append(c)
			result.append(a)
			result.append(c)
			result.append(b)
			result.append(c)
			return "".join(result)

		if p >s and r>s:
			for i in range(0,p/4):
				result.append(a)
				result.append(b)
				result.append(c)
			result.append(a)
			result.append(b)
			return "".join(result)
		if p >r and s>r:
			for i in range(0,p/4):
				result.append(a)
				result.append(b)
				result.append(c)
			result.append(a)
			result.append(c)
			return "".join(result)
		if r >p and s>p:
			if n == 3:
				return b+c
			for i in range(1,p/4):
				result.append(a)
				result.append(b)
				result.append(c)
			result.append(b)
			result.append(a)
			result.append(c)
			result.append(b)
			result.append(c)
			return "".join(result)



for i in range(1,t+1):
	n, r, p, s = [int(x) for x in f.readline().split(" ")]
	new_file.write("Case #"+str(i)+ ": "+str(good_start(n,r,p,s))+"\n")