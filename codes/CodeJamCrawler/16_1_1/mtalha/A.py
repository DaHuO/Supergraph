#from __future__ import print_function
import sys;
if __name__ == '__main__':
	cases = int(sys.stdin.readline())
	lm=[]
	for i in range(cases):
		lm=(sys.stdin.readline())
		x=[]
		o=0;
		for k in range(len(lm)-1):
			if o==0:
				x=lm[k]
				o=o+1
			else:
				if(lm[k]>=x[0]):
					x=lm[k]+x;
				else:
					x=x+lm[k]
		print "Case #"+str(i+1)+": "+str(x)
