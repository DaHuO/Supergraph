#!usr/bin/python2
import sys
import math

def main():
	print "Case #1:\n"
	cases = int(raw_input())
	for case, line in enumerate(sys.stdin):
		n, j = map(int, line.split())
		found = 0
		coinnumber = 0
		start = 2**(n-1) + 1
		while found < j:
			coin = start + (coinnumber * 2)
			bincoin = bin(coin)[2:]
			isjamcoin = True
			divisors = [bincoin]
			for base in range(2, 11):
				basecoin = int(bincoin, base)
				if basecoin % 2 == 0:
					divisors.append("2")
				else:
					for i in xrange(3, int(math.sqrt(basecoin))+1, 2):
						if basecoin % i == 0:
							divisors.append(str(i))
							break
					else:
						isjamcoin = False
						break
			if isjamcoin:
				print "\t" + " ".join(divisors)
				found += 1
			coinnumber += 1
			

if __name__ == "__main__":
	main()
