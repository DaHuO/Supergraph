import sys

def subprocess(s):
    ar = []
    for c in s:
	ar.append(c)

    res = 0
    p = 0
    flag = True
    while p < len(ar) and ar[p] == '-':
	p += 1
	flag = False

    if not flag:
	res = 1

    t = len(ar)-1
    while t >= p and ar[t] == '+':
	t -= 1
       
    while p <= t:
	while p <= t and ar[p] == '+':
	    p += 1
	while p <= t and ar[p] == '-':
	    p += 1
	res += 2

    return res

def rev(c):
    if c == "+":
	return "-"
    else:
	return "+"

def process(s):
    return subprocess(s)
    '''
    rs = ""
    for i in xrange(len(s)-1, -1, -1):
	rs += rev(s[i])
    return min(subprocess(rs)+1, subprocess(s))
    '''

def main():
    f = open(sys.argv[1])
    t = int(f.readline().strip())
    for i in xrange(t):
	line = f.readline().strip()
	res = process(line)
	print "Case #"+str(i+1)+": "+str(res)
    f.close()

if __name__ == "__main__":
    main()
