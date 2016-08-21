import sys

def findNum(s):
    if s <= 0:
	return "INSOMNIA"
    k = set()
    base = s
    s = 0
    while len(k) < 10:
	s += base 
	for c in str(s):
	    k.add(c)
    return s

def main():
    f = open(sys.argv[1])
    t = int(f.readline().strip())
    
    for i in xrange(t):
	line = f.readline()
	s = int(line.strip())
	res = findNum(s)
	print "Case #"+str(i+1)+": "+str(res)	
    f.close()

if __name__ == "__main__":
    main()
