import math

def solve(s):
    count = 0
    n = max(s.find("-"),s.find("+"))
    while(n!=0):
        s = flip(s,n)
        count+=1
        n = max(s.find("-"),s.find("+"))
    if(s[0]=="-"):
        count+=1
    return count


def flip(s,n):
    return s[0:n][::-1].replace("+","p").replace("-","+").replace("p","-")+s[n:]

if __name__ == "__main__":
	testcases = input()

	for caseNr in xrange(1, testcases+1):
		s = raw_input()
		print("Case #%i: %s" % (caseNr, solve(s)))
