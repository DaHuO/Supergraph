n = input()

numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def canAdd(d, i):
	d2 = dict(d)
	for c in numbers[i]:
		if not (c in d):
			return (False, d2)
			
		if d[c] > 0:
			d[c] -= 1
		else:
			return (False, d2)
			
	return (True, d)

def addDict(d, s):
	for c in numbers[s]:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1
	
	return d
	
d = {}
res = ""
def solve():
	global d
	global res
	#print "solve",d,res
	if sum(d.values()) == 0:
		return res
		
	for i in range(10):
		keep, d = canAdd(d, i)
		if keep:
			res += str(i)
			#print "res", res
			#print "dict", d
				
			aux = solve()
			if aux:
				return aux
	
	if sum(d.values()) != 0:
		d = addDict(d, int(res[-1]))
		res = res[:-1]
	
	
for case in range(n):
	s = raw_input()

	for c in s:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1

	res = ""
	res = solve()
	
	print "Case #"+str(case+1)+":", res