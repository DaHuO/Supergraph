def dec_to_bin(x):
    return str(bin(x)[2:])
    
def convert(s, base):
	s = s[::-1]
	ret = 0
	mul = 1
	for i in s:
		if i == '1':
			ret += mul
			mul *= base
		else:
			mul *= base
	return ret

tc = int(raw_input())
print "Case #1:"
while tc:
	tc -= 1
	n,jam = map(int,raw_input().split())
	start = pow(2,n-1) + 1
	end = pow(2,n) - 1
	ct = 0
	for i in range(start, start + 4000, 2):
		s = dec_to_bin(i)
		found = False
		ans = []
		ans.append(s)
		for j in range(2,11):
			found = False
			num = convert(s, j)
			for k in range(2,1000):
				if num % k == 0:
					ans.append(k)
					found = True
					break
			if found == False:
				break
		if found == True:
			ct += 1
			for k in ans:
				print k,
			if ct == jam:
				break
			print ""
