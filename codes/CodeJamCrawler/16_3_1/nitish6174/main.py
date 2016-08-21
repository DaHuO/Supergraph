from math import *
import re

t = int(input())

for itr in range(0,t):
	n = int(input())
	line = (input()).split(' ')
	a = []
	for i in range(0,n):
		a.append(int(line[i]))

	print("Case #"+str(itr+1)+": ",end="")
	max1 = 0
	for i in range(0,n):
		if a[i]>a[max1]:
			max1 = i
	max2 = 0
	if max1==0:
		max2=1
	for i in range(0,n):
		if a[i]>a[max2] and i!=max1:
			max2 = i
	while a[max1]!=a[max2]:
		c = (chr(ord('a')+max1)).upper()
		if a[max1]-a[max2]==1:
			print(c+" ",end="")
			a[max1]-=1
		else:
			print(c+c+" ",end="")
			a[max1]-=2
	for i in range(0,n):
		c = (chr(ord('a')+i)).upper()
		while a[i]!=0 and i!=max1 and i!=max2:
			if a[i]==1:
				print(c+" ",end="")
				a[i]-=1
			else:
				print(c+c+" ",end="")
				a[i]-=2
	while a[max1]!=0:
		c = (chr(ord('a')+max1)).upper()
		c2 = (chr(ord('a')+max2)).upper()
		print(c+c2+" ",end="")
		a[max1]-=1
	print('')