def GetPossible(d, first, last):
	cur = d
	result = []
	i = 1
	
	if cur == 0:
		return []

	while cur <= 10:
		if cur == 10:
			if first:
				result.append(0)
			if last:
				result.append(1)
		else:
			result.append(cur)
		i = i+1
		cur = d * i
		

	return result

def GetAnswer(n):
	fullset= map(str, range(0,10))
	result = []
	for i in range(1,10000):
		cur = n * i
		result.extend(list(set(list(str(cur)))))
		result = list(set(result))
		result.sort()
		
		if fullset == result:
			return cur
	return "INSOMNIA"

fi = open("input","r")
fo = open("output","w")
t = int(fi.readline().strip())



for i in range(t):
	fo.write("Case #{0}: {1}\n".format(i+1,  GetAnswer(int(fi.readline().strip()))))





fi.close()
fo.close()	