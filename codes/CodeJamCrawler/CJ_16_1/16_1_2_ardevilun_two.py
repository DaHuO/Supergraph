import sys
T=int(sys.stdin.readline())
for z in range(1,T+1):
	N=int(sys.stdin.readline())
	main=[]
	for b in range(0,2*N-1):
		l = [int(x) for x in sys.stdin.readline().split(" ")]
		for q in l:
			main.append(q)

	slave1=[]
	slave2=[]
	for a in main:
		if a not in slave1:
			slave1.append(a)
			if main.count(a)%2 !=0:
				slave2.append(a)

	final = sorted(slave2)
	print "Case #"+str(z)+":",
	for a in final:
		print a,
	print ("\n")


	


