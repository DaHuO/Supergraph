import math

def solve(n):
    if(n==0):
        return "INSOMNIA"
    s = set()
    nn = n
    while len(s)<10:
        s = s.union(set(str(nn)))
        nn+=n
    return str(nn-n)

if __name__ == "__main__":
	testcases = input()

	for caseNr in xrange(1, testcases+1):
		n = int(raw_input())
		print("Case #%i: %s" % (caseNr, solve(n)))
