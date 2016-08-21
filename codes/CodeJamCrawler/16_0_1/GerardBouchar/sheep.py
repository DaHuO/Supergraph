import pickle

def updateFound(n,found):
	strN=str(n)
	for c in strN:
		found[c]=True

def getAnswer(n):
	if n == 0 :
	 	return "INSOMNIA"
	found = {"0":False,"1":False,"2":False,"3":False,"4":False,"5":False,"6":False,"7":False,"8":False,"9":False}

	it=0
	while not all(found.values()) :
		it+=n
		updateFound(it,found)

	return str(it)

for N in range(int(input())) :
	n=int(input())
	print("Case #"+str(N+1)+": "+getAnswer(n))


