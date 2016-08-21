import sys
import os
t=int(input())
o=t;
while t:
	s=list(raw_input())
	n=len(s)
	i=n-1
	a=0
	while i>=0:
		#print s[i]
		#a=False
		if s[i]=="-":
			if s[0]=="-":
				#print s
				sl=s[0:i+1]
				sl.reverse()
				s[0:i+1]=sl
				#print s
				for j in xrange(0,i+1):
					if s[j]=="-":
						s[j]="+"
					else:
						s[j]="-"
				a=a+1
				#print a
			else:
				#print "h:%s" %s[i]
				if s[i-1] == "+":
					sl=s[0:i]
					sl.reverse()
					s[0:i]=sl
					#print s
					for j in range(0,i):
						if s[j]=="-":
							s[j]="+"
						else:
							s[j]="-"
					i=i+1
					a=a+1
				else:
					f=i-1
					while(f > 0):
						if(s[f]=="+"):
							break
						f=f-1
					sl=s[0:f+1]
					sl.reverse()
					s[0:f+1]=sl
					for j in range(0,f+1):
						if s[j]=="-":
							s[j]="+"
						else:
							s[j]="-"
					i=i+1
					a=a+1
				#print a
			
		i=i-1
		#print s
	print "Case #%d: %d" %(o-t+1,a)

	t=t-1
