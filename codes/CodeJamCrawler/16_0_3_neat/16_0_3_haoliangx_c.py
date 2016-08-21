def first_divisor(N):
	for i in range(2, int(N**0.5)+2):
		if N%i==0:
			return i
	return -1

def first_d(n):
	if n == 2 or n == 3: return -1
	if n < 2 or n%2 == 0: return 2
	if n < 9: return -1
	if n%3 == 0: return 3
	r = int(n**0.5)
	f = 5
	while f <= r:
		#print '\t',f
		if n%f == 0: return f
		if n%(f+2) == 0: return f+2
		f +=6
	return -1

def solve_single(n):
	ss = bin(n)[2:]
	s = ['1' + '0'*(N - 2 - len(ss)) + ss + '1', ]
	for i in range(2, 11):
		t = int(s[0], i)
		d = first_d(t)
		if d == -1:
			break
		else:
			s.append(str(d))
	return s

def handler(signum, frame):
	raise Exception("")

import signal

def solve(N, J):
	ret_list = []
	l = int('0'*(N-2), 2)
	u = int('1'*(N-2), 2)
	signal.signal(signal.SIGALRM, handler)
	for n in xrange(l, u+1):
		signal.alarm(1)
		try:
			s = solve_single(n)
		except Exception:
			signal.alarm(0)
			continue
		signal.alarm(0)
		if len(s) == 10:
			ret_list.append(s)
			#print len(ret_list),
			for t in s:
				print t,
			print
		if len(ret_list) == J:
			break
	return ret_list


'''
items = []
n = int(raw_input())
for i in range(n):
	s = raw_input()
	N, J = s.split(' ')
	items.append((int(N), int(J)))

'''
items = [(16, 50)]
i = 1
for N, J in items:
	print "Case #%d:" % i
	#for r in solve(N, J):
	#	for t in r:
	#		print t,
	#	print
	solve(N, J)
	i += 1
