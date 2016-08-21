import sys

def solve(n):
    if n == 0:
        return 'INSOMNIA'
    seen = set(str(n))
    last, counter = n, 1
    while len(seen) < 10:
        counter += 1
        last = counter * n
        seen |= set(str(last))
    return last
    
def main(inFile):
    with open(inFile) as inp, open(inFile.replace('.in', '.out'), 'w') as out:
        T = int(inp.readline().strip())
        for t in xrange(T):
            N = int(inp.readline().strip())
            out.write('Case #%d: %s\n' % (t + 1, solve(N)))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: %s input.in' % sys.argv[0])
    main(sys.argv[1])
