#!usr/bin/env python
from __future__ import print_function
from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *

def main():
	cases=int(raw_input())
	for i in xrange(cases):
		n=int(raw_input())
		if n==0:
			print("INSOMNIA")
			continue
		condition=0
		counter=1
		digits=[0 for d in xrange(0,10)]
		while condition==0:
			num=n*counter
			back=num
			while num!=0:
				d=num%10
				num=num/10
				digits[d]=1
				if 0 in digits:
					continue
				else:
					fd=back
					break
			if 0 in digits:
				counter+=1
				condition=0
			else:
				condition=1
		print("Case #",i+1,":"," ",fd,sep="")

if __name__=='__main__':
	main()