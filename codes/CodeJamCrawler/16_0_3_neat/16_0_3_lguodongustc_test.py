#!/usr/bin/python

from math import sqrt
from math import pow

def geneDiv(number):
	sqn=int(sqrt(number))
	for i in range(2,sqn+1):
		if number%i == 0:
			return i
	return 0;


def calcNum (num, base, len):
	number=0
	for i in range(0,len):
		if num[len-i-1] == 1:
			number+=pow(base,i)

	return number

def geneJC(cas, N, J):
	print "Case #{}:".format(cas)	
	i=0;
	for k in range(0,int(pow(2,N-2))):
		temp=k;
		div=[0]*9
		num=[0]*N
		num[0]=1
		num[N-1]=1
		for p in range(1,N):
			if(temp%2!=0):
				num[N-1-p]=1
			temp/=2
			if(temp==0):
				break
		for p in range(2,11):
			number=calcNum(num,p,N)
			div[p-2]=geneDiv(number)
			if div[p-2]==0:
				break
		if (p == 10)and(div[p-2]!=0):
			i+=1
			print int(number),
			for p in range(0,9):
				print("%d" % div[p]),
			print
		if i==J:
			break;

t = int(raw_input())
for i in range(1,t+1):
	N, J = [int(s) for s in raw_input().split(" ")]
	geneJC(i,N,J)




