#!/usr/bin/python

t = int(raw_input())

for i in range(0,t):
	s = str(raw_input())
	
	a = ""

	for x in s: 
		if len(a) == 0:
			a = a + x
		else:
			#print "x=",x,"a=",a
			
			if a[0] <= x:
				a = x + a
			else:
				a = a + x
			'''
			for sc in range(0,len(a)):
				print sc
				print "x=",x,"a[sc]=",a[sc]
				if x > a[sc]:
					break
			a = a[:sc] + x + a[sc:]
			print a
			'''

			#print a
	print "Case #" + str(i+1) + ": " + str(a)
		

