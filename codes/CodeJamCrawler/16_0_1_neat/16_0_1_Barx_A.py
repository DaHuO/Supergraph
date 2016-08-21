
def solve(N):
	if N==0:
		return 'INSOMNIA'
	t=N
	c = set()
	for x in str(t):
		c.add(int(x))

	while len(c) < 10:
		#print c
		t += N
		for x in str(t):
			c.add(int(x))
        		
	return str(t)

    
def main(source, dest):
    fd = open(source, 'r')
    fo = open(dest, 'w')
    T = int(fd.readline())
    for i in range(1,T+1):
        N = int(fd.readline())
        result = solve(N)
	
        print 'Case #' + str(i) + ': ' + result + '\n',
        fo.write('Case #' + str(i) + ': ' + result + '\n')
	
    fd.close()
    fo.close()


if __name__ == "__main__":
	filename = os.path.basename(sys.argv[1])
	source = sys.argv[1]
	dest = os.path.join(sys.argv[2], filename.replace(".in.txt",".out.txt"))
	main(source, dest)