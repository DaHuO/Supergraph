import math

def solve(k,c,s):
    if(c==1):
        if(s<k):
            return "IMPOSSIBLE"
        l = list(map(str,range(1,k+1)))
    else:
        if(s<math.ceil(k/2)):
            return "IMPOSSIBLE"
        l = []
        for i in range(1, k+1,2):
            if(i==k):
                l+=[str(check1(k,c,i))]
            else:
                l+=[str(check2(k,c,i,i+1))]
    return " ".join(l)

def check2(k,c,n1,n2):
    return (n1-1)*(k**(c-1))+check1(k,c-1,n2)

def check1(k,c,n):
    ret = 1
    for i in range(0,c):
        ret += (n-1)*(k**i)
    return ret

if __name__ == "__main__":
	testcases = input()

	for caseNr in xrange(1, testcases+1):
		inp = list(map(int, raw_input().split(" ")))
		print("Case #%i: %s" % (caseNr, solve(inp[0], inp[1], inp[2])))
