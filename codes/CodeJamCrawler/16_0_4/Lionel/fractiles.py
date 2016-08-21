import sys

def main():
    f = open(sys.argv[1])
    t = int(f.readline().strip())

    for i in xrange(t):
	line = f.readline().strip()
	sp = line.split()
	k = int(sp[0])
	c = int(sp[1])
	s = int(sp[2])
	
	base = pow(k, c-1)
	if c == 1:
	    base = 0

	s = ""
	for j in xrange(k):
	    s += str(base*j+j+1)
	    if j < k-1:
		s += " "
	print "Case #"+str(i+1)+": "+s

    f.close()

if __name__ == "__main__":
    main()
