import sys
inp = open("in.txt")
out = open("out.txt","w+")
sys.stdout = out
tc = 0

class ImpossibleError(Exception):
	pass

t = int(inp.readline())

def print_case(case, result):
	print "Case #%d: %s" % (case, str(result))

def debug(message):
	if len(sys.argv) > 1 and sys.argv[1] == "silent":
		return
	sys.stdout = sys.__stdout__
	print message
	sys.stdout = out


for tc in xrange(t):
    n = int(inp.readline())
    if n == 0:
        print_case(tc+1, "INSOMNIA")
        continue
    
    seen = [False] * 10
    i = 0
    while not all(seen):
        i += 1
        for c in str(i*n):
            seen[int(c)] = True
    
    print_case(tc+1, i*n)
        