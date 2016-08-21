from fractions import gcd

inf = open('A-large.in', 'r')
outf = open('A-large.out', 'w')

def isMajority(x):
	return max(x) > float(sum(x)/2)

for it in xrange(int(inf.readline())):
	p = int(inf.readline())
	parties = [chr(x+65) for x in xrange(p)]

	senators = map(int, inf.readline().split(' '))
	magic_number = sum(senators)/p
	print parties, senators, magic_number
	ans=""

	while sum(senators)!=0:
		hcf = reduce(gcd, senators)
		index = [i[0] for i in sorted(enumerate(senators), key=lambda x:x[1], reverse=True)]
		if hcf >= 2:			
			senators[index[0]]-=1
			senators[index[1]]-=1
			print parties[index[0]]+parties[index[1]]
			ans += parties[index[0]]+parties[index[1]]+" "
		elif hcf == 1:
			if senators.count(1) == 2 and senators.count(0)+senators.count(1) == p:
				senators[index[0]]-=1
				senators[index[1]]-=1
				print parties[index[0]]+parties[index[1]]
				ans += parties[index[0]]+parties[index[1]]+" "
			else:
				senators[index[0]]-=1
				print parties[index[0]]
				ans += parties[index[0]]+" "
		# print senators
		# if isMajority:
		# 	print 'something is wrong'

	outf.write('Case #%d: %s\n'%(it+1,ans))


outf.close()