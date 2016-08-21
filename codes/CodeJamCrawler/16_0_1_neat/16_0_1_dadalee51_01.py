import fileinput
import collections

def join(arr):
	outStr=""
	for i in arr:
		outStr= outStr + str(i) + " "
	return outStr.strip()


def solve(fileName):
	fout = open(fileName+".pythout", 'w')
	with open(fileName, 'r') as f:
		T = int(f.readline())
		for ci in range(T):
			print "----------case ",ci+1
			m = f.readline()
			print m
			a=int(m)
			b=a
			d = set()
			ans=""
			for i in range(1000000):
				b=(i+1)*a
				#print b
				c = set(str(b))
				d = c | d
				if len(d)==10 :
					print "done" , b
					ans = str(b)
					break
				else:
					ans = "INSOMNIA"
			fout.write("Case #"+str(ci+1)+": " +ans+ "\n")	
	return;

#solve here.
#solve("test")
#solve("small")
solve("large")