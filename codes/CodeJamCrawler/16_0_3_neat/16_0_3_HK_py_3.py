import math as m
import sys

def isprime(N):
	N= int(N)
	if N == 0 or N == 1:
		return True

	up = int(m.sqrt(N))
	for i in range(2,up+1):
		if N % i == 0:
			return True

	return False

# print isprime(sys.argv[1])

def get_non_trev_div(N):

	up = int(m.sqrt(N))

	# for i in range(2,up+1):
	st = 2
	while True:
		# print i
		if N % st == 0:
			return st

		st +=1 
		# print st
		if st > up or st > 10000:
			break

	return False

def get_devs(s):
	s = list(s)
	s = [int(d) for d in s]

	ret_l = []
	for base in range(2,11):

		num = 0
		for i in range(len(s)):
			if s[i] != 0:
				num += ((base**(len(s)-1-i))*s[i])

		nn = get_non_trev_div(num)
		# print num,base,nn
		if nn == False:
			return []
		# print num , nn

		ret_l.append(nn)
	return ret_l

def gen(N):
	if N == 1:
		return ['1']

	ps = gen(N-1)

	r = []
	for k in ps:
		r.append('0'+k)
	for k in ps:
		r.append('1'+k)
	return r

f = open("C-large.in" , "r")

lines = f.readlines()

T = int(lines[0])
nj = lines[1].split(" ")
N = int(nj[0])
J = int(nj[1])

# all_s = gen(N-1)
f = open("large.op","w")

print "Case #1:"
f.write("Case #1:\n")
cnt = 0
for a in all_s:
	print a
	r = get_devs(a)
	# print a
	# exit()
	if r != []:
		cnt += 1
		newa = a#'0'*(N-10)+a
		print newa,
		f.write(str(newa)+" ")
		for rr in r:
			f.write(str(rr)+" ")
			print rr,
		f.write("\n")
		print cnt
		if cnt == J:
			break
		print ""
	# sa = raw_input()

