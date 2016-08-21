def genstr(l, k):
	for i in range(1, k):
		if(l[i]=='1'):
			l[i] = '0'
		else:
			l[i]='1'
			break

def factgen(l, k, factl):
	for i in range(2, 11):
		val = 1
		num = 1
		for j in range(1, k):
			num = num*i
			if(l[j]=='1'):
				val = val + num
		factl[i-2] = val

t = int(raw_input())

N, J = map(int, raw_input().split())

m = N/2

l=['0']*m
l[0] = '1'
l[m-1] = '1'

print "Case #1:"
for i in range(J):
	genstr(l, m-1)
	l1 = "".join(l)
	l1 = l1[::-1]
	print l1+l1, 
	factl = [0]*9
	factgen(l, m, factl)
	for i in range(8):
		print factl[i],
	print factl[8]
