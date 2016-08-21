def solve(n):
    n=int(n)
    mySet=set()
    if n==0:
        return "INSOMNIA"
    else:
        count=1
        while len(mySet)<10:
            myNum=count*n
            myNumString=str(myNum)
            for c in myNumString:
                mySet.add(c)
            count+=1
        return str((count-1)*n)
            

if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(1, testcases+1):
		cipher = raw_input()
		print("Case #%i: %s" % (caseNr, solve(cipher)))
