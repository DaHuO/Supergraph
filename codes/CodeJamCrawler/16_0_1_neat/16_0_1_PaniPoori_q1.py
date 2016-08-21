import sys


def findsleep(a,tc):
	s = set([0,1,2,3,4,5,6,7,8,9])
	i =0
	print "Case #%d:" % (tc),
	if a==0:
		print "INSOMNIA"
		return
	i = 1
	while(s):
		number = i * a
		digits = map(int,str(number))
		for digit in digits:
			s.discard(digit)
		i+=1
	print number

if __name__ == '__main__':
	# inp =[0,1,2,11,1692]
	
	# for item in inp:
	f = open("A-large.in","r")
	first = 0
	for line in f:
		ntc = int(line.strip())
		if(first):
			findsleep(ntc,first)
		
		first+=1
