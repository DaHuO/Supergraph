def transpose(str1):
	str1 = str1.replace('-','*')
	str1 = str1.replace('+','-')
	str1 = str1.replace('*','+')
	return(str1)

def p1(str1):
	cnt = 0
	l = len(str1)
	for i in range(l):
		li = len(str1) -1
		last = str1[li]
		if last == '-':
			str1 = transpose(str1[:-1])
			cnt += 1
		else:
			str1 = str1[:-1]
	return (cnt)

T=int(input())
for t in range (T):
	str1 = raw_input()
	cnt = p1(str1)
	print ('Case #%d: %d' %(t+1,cnt))
