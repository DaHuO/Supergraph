import math
import random

trials = 20

def is_prime(n):
	assert n >= 2
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	s = 0
	d = n - 1
	while True:
		q,r = divmod(d,2)
		if r == 1:
			break
		s += 1
		d = q
	assert 2 ** s * d == n - 1
	def try_composite(a):
		if pow(a,d,n) == 1:
			return False
		for i in range(s):
			if pow(a,2 ** i * d,n) == n - 1:
				return False
		return True
	for i in range(trials):
		a = random.randrange(2,n)
		if try_composite(a):
			return False
	return True

ff = open('input.in','r').read()
fw = open('output.in','w')

a1 = ff.split('\n')
t = int(a1[0])
a2 = a1[1].split(' ')
n,m = int(a2[0]),int(a2[1])

for tc in range(t):
	fw.write("Case #" + str(tc + 1) + ":\n")
	for i in range(2 ** (n - 1), 2 ** (n - 1) + 100000):
		if m == 0:
			break
		num = i
		s = ""
		for j in range(n):
			s = s + str(num % 2)
			num = num / 2
		s = s[::-1]
		if s[0] != '1' or s[n - 1] != '1':
			continue
		ans = []
		flag = 0
		for j in range(2,11):
			num = 0
			mul = 1
			for k in range(n - 1,-1,-1):
				if s[k] == '1':
					num = num + mul
				mul = mul * j
			if is_prime(num) == True:
				flag = 1
				break
			else:
				flag1 = 0
				for k in range(2,500):
					if num % k == 0:
						flag1 = 1
						ans.append(k)
						break
				if flag1 == 0:
					flag = 1
					break
		if flag == 1:
			continue
		else:
			for j in range(len(ans)):
				s = s + ' ' + str(ans[j])
			fw.write(s + '\n')
			m -= 1