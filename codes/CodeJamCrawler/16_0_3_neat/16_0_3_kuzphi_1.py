
cnt = 50
w = [0] * 14
def Get_number(a , base):
	ans = 0
	for x in a:
		ans = ans * base + x
	return ans

def dfs(pos):
	global cnt
	if cnt == 0:
		return
	if pos == 14:
		number = [1] + w + [1]		
		fac = []
		for b in xrange(2,11):
			num = Get_number(number , b)
			i = 2
			ck = 0
			while i * i <= num:
				if num % i == 0:
					ck = 1
					break
				i+=1
			if ck == 0:
				return
			fac.append(i)
		cnt -= 1
		print reduce(lambda x, y: 10 * x+y,number),		
		for f in fac: 
			print f,
		print ''
		return 	
	dfs(pos + 1)
	w[pos] = 1
	dfs(pos + 1)
	w[pos] = 0

# T = input()
T = 1
for cas in xrange(1,T+1):	
	print 'Case #'+str(cas)+":"
	dfs(0)