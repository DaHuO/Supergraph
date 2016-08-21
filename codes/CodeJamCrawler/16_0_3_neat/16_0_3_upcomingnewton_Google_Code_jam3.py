import sys
import math


def is_prime(x):
	# try finding factor between 0 to min(root(x),10,000,000)
	for i in xrange(2,min(int(math.sqrt(x)+1),1000)):
		if x%i==0:
			return i
	return True

def convert_num_to_base(l,base):
	return int(l,base)

def find_sol(n,j):
	ans = []
	for x in xrange(0,2**30-1):
		s1 = str(bin(x))[2:]
		s = "1" + "0"*(30-len(s1)) + s1 + "1"
		# convert in all bases and check if it is prime
		num_bases = [is_prime(convert_num_to_base(s,base)) for base in xrange(2,11)]
		if True not in num_bases:
			ans.append([s] + num_bases)
			if len(ans) == j:
				break
	return ans

if __name__ == "__main__":
	#data = [x.strip() for x in sys.stdin.readlines()]
	#n,j = map(int,data[1].split())
	n,j = 32,500
	ans = find_sol(n,j)
	print "Case #1:"
	for x in ans:
		print " ".join(map(str,x))
