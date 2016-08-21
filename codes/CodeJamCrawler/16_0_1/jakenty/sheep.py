#!/usr/bin/python2
from sets import Set
def getlastnum(n):
	num=n
	if num<1:
		return "INSOMNIA"
	nums = Set([0,1,2,3,4,5,6,7,8,9])
	i =1
	while(i<100):
		x=num
		while(x>0):
			t = x%10
			nums.discard(t)
			if len(nums)<1:
				return num
			x = x/10

		num=n*i
		i+=1
	if len(nums)<1:
		return num
		
lines = open("A-large.in").readlines()
#lines = open("A-small-attempt1.in").readlines()
#lines = open("input.txt").readlines()

f = open('ouput.txt', 'w')
t = int(lines[0])
for i in range(1,t+1):
	num = int(lines[i])
	lastnum = getlastnum(num)
	f.write("Case #%s: %s"%(i,lastnum))
	if (i<t):
		f.write("\n")
f.close()