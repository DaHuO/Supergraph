#!/usr/bin/python
import sys



cases = int(sys.stdin.readline().rstrip("\n"),10)




def  r_divsor2(number):
	r=-1;
	for i in range(2,number/2):
		if number%i==0:
			r=i
			break
	return r;

def  r_divsor(n,system,primes):
	number=int(n,system)
	r=-1;
	for i in primes:
		if number%i==0:
			r=i
			break
	return r;


def  primes_til_16():
	r=[2]
	
	for i in range(3,16000):
		if r_divsor2(i)==-1:
			r.append(i)
	return r


for c in range(0,cases):
	line=sys.stdin.readline().rstrip("\n").split()
	N=int(line[0],10)
	J=int(line[1],10)
	nnn=N-2
	s_nnn="0"+str(nnn)+"b"
	j_star=0

	min_str="".join(['0' for i in range(0,nnn)])
	max_str="".join(['1' for i in range(0,nnn)])

	max_n=int(max_str,2)
	min_n=int(min_str,2)
	
	print("Case #"+str(c+1)+":")

	primes=primes_til_16()

	i=min_n

	while j_star!=J and i<=max_n:
		status = True
		j_coin = "1"+format(i,s_nnn)+"1"
		divisor=[]
		for s in range(2,11):
			d=r_divsor(j_coin,s,primes)
			if d==-1:
				status=False
				break	
			else:
			   divisor.append(d)
			
		if status:
			str_=str(j_coin)
			for df in divisor:
				str_=str_+" "+str(df)
			print(str_)
			j_star=j_star+1
		i=i+1

