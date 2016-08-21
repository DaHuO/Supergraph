import math
import re
def inBase(n,b):
	p = 1
	c = 0
	while (n>0):
		c+= (n%10)*p
		p = p*b
		n = n/10
	return c

def is_prime(n):
	u = math.floor(math.sqrt(n))
	d = 2
	while d <= u:
		if n%d == 0:
			return d
		d+=1
	return -1

def is_coin_jam(n):
	A= [is_prime(inBase(n,i)) for i in range(2,11)]
	if -1 not in A:
		return A
	else :
		return []

def calc_p(a):
	A = []
	for x in range(int(math.pow(2,a))):
		if int(bin(x)[2:].zfill(a))%2 == 1 and int(bin(x)[2:].zfill(a))/int(math.pow(10,a-1)) :
			A.append(int(bin(x)[2:].zfill(a)))
	#print len(A)
	return A

def find_coins(a,j):
	ps = calc_p(a)
	cnt = 0
	i = 0
	B =[]
	while cnt < j and i < len(ps):
		A = is_coin_jam(ps[i])
		if len(A) > 0:
			s = ""
			for kk in range(len(A)):
				s+=" "+str(A[kk])
			B.append(str(ps[i]) +s)
			cnt+=1
		i+=1
	return B

#print find_coins(6,3)
def read_input(input1,output):
	o = open(input1,"r")
	w = open(output,"w")
	l = o.readline()
	num_of_cases =  int(re.findall(r'[0-9]+',l)[0])
	for i in range(1,num_of_cases+1):
		l = o.readline()
		nums = re.findall(r'[0-9]+',l)
		a = int(nums[0])
		j = int(nums[1])
		w.write("case #%d:\n" %i)
		B = find_coins(a,j)
		for i in B:
			w.write(i+"\n")
	w.close()
if __name__ == "__main__":
	read_input("C-small-attempt0.in","C_small.out")





