def solve(P):
    s = {}
    for p in P:
        for i in p:
            if not i in s:
                s[i] = 0
            s[i] += 1
    missing = [k for k,v in s.iteritems() if v%2==1]
    
    
    missing.sort()
    return " ".join([str(m) for m in missing])

def main(source, dest):
    with open(source, 'r') as fd, open(dest, 'w')as fo:
        T = int(fd.readline())
        for i in xrange(1,T+1):
            N = int(fd.readline())
            p = []
            for _ in xrange(2*N-1):
                p.append([int(x) for x in fd.readline().rstrip().split(' ')])
			
            result = solve(p)
            print 'Case #' + str(i) + ': ' + result
            fo.write('Case #' + str(i) + ': ' + result + '\n')

if __name__ == "__main__":
	filename = os.path.basename(sys.argv[1])
	source = sys.argv[1]
	dest = os.path.join(sys.argv[2], filename.replace(".in.txt",".out.txt"))
	main(source, dest)