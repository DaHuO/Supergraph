import sys

def counting_sheep(argv):
	with open(argv[0], 'r') as f:
		t = int(f.readline())
		for i in range(t):
			n = f.readline().strip()
			j = 1
			digits = set()
			if (n == "0"):
				print "Case #%d: INSOMNIA" % (i+1)
				continue
			while True:
				num = str(j*int(n))
				digits = digits | set([x for x in num])
				if len(digits) == 10:
					print "Case #%d: %s" % ((i+1), num)
					break
				j = j + 1

if __name__ == "__main__":
	counting_sheep(sys.argv[1:])