def numTest(b,n):
    for i in range(len(n)):
        b[n[i]]=True
        #print("b: %d" % (b[n[i]]))
        #print ("b value: %b %b" % (b[0],b[1]))
    return b

def count(n,n1):
    b=[False,False,False,False,False,
    False,False,False,False,False]
    #for i in range(100):
    for i in range(100):
        n2=int(n1)*(i+1)
        n = [(ord(v) - ord('0')) for v in str(n2)]

        c=numTest(b,n)
        for x in range(10):
            b[x] = b[x] | c[x]
        ab = True
        for x in range(10):
            ab = b[x] and ab
        if(ab == True): return n2

    #for i in range(10):
     #   print("b: %d" % (b[i]))

    return 0

if __name__ == "__main__":
	tcases = input()

	#print("%s" % (testcases))
	for caseNr in range(1, int(tcases)+1):
		n1 = input()
		n = [(ord(v) - ord('0')) for v in n1]
		#print("n: %d" % (n[0]))
		ans=count(n,n1)
		#if n[0]==0 and len(n)==1: print("Case #%i: %s" % (caseNr,"INSOMNIA"))
		if ans==0: print("Case #%i: %s" % (caseNr,"INSOMNIA"))
		else: print("Case #%i: %d" % (caseNr,ans))