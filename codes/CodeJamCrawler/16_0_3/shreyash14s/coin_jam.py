from math import sqrt, ceil
def pz(s, n):
	l = len(s)
	return '0' * (n-l) + s

def gen_coin(n):
	if n <= 2:
		yield '11'
		return
	for i in range(int('1'*(n-2), 2)+1):
		yield '1' + pz(bin(i)[2:], n-2) + '1'

# def indx(i):
# 	j = 0
# 	while i > soe[j]:
# 		j+=1
# 	if i == soe[j]:
# 		return j
# 	return -1

def prime(n, i=3):
	# try:
	# 	s = soe.index(i)+1
	# except:
	# 	s = 0
	# for i in range(s, len(soe)):
	# 	if n % soe[i] == 0:
	# 		return i
	# return -1
	if n % 2 == 0:
		return 2
	sqn = ceil(sqrt(n))
	while i < sqn:
		if n % i == 0:
			return i
		i += 2
	return 0

def s_of_e(n):
	a = [1]*(n+1)
	# a = 2**(n+1)-1
	# i = 1
	# c = 0
	# cn = a+1
	# while i < cn:
	# 	if a & i:
	# 		j = i
	# 		while j < n:
	# 			a = a & ~j
	# 			j <<= c
	# 	i <<= 1
	# 	c += 1
	for i in range(2, int(sqrt(n+1))+1):
		if a[i]:
			for j in range(i*i, n+1, i):
				a[j] = 0
	b = [i for i in range(2, n+1) if a[i]]
	return a, b

d = set()

def f(n, j, s=''):
	ji = 0
	l1 = [0] * (j)
	g = gen_coin(n)
	if s:
		while next(g) != s:
			pass
	ji = 0
	for i in g:
		l = []
		kl = []
		# print(i)
		for m in range(2, 11):
			k = int(i, m)
			kl.append(k)
			# if soea[k]:
			# 	break
			# p = prime(k)
			# if p == -1:
			# 	break
			if k in d:
				break
			p = prime(k)
			if not p:
				d.add(k)
				break
			d.add(p)
			l.append(p)
		else:
			# print(i)
			if ji >= len(l1):
				break
			print(i, end=' ')
			for j in l:
				print(j, end=' ')
			print()
			# for j in kl:
			# 	print(j, end=' ')
			# print()
			l1[ji] = [i] + l
			ji += 1
		if ji != j:
			pass
		else:
			break
	return l1

t = input()
n, j = input().split()
n = int(n)
j = int(j)
# g = input()
# print(n, j)
# soea, soe = s_of_e(int('1'*n))
# soe.append(int('1'*n))
print("Case #1:")
l = f(n, j)
# print(l)
# for i in l:
# 	for j in i:
# 		print(j, end=' ')
# 	print()
