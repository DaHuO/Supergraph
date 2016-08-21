fp = open("case.txt","r")
out = open("result.txt","w")

cache = fp.readlines()
cache = cache[1:]
#print N
N=[]
for i in cache:
	N.append(int(i))

test_no=1
for test in N:
	check=[0,0,0,0,0,0,0,0,0,0]
	count=1
	while True:
		M=test*count
		if M==0:
			x = "Case #%d: INSOMNIA\n" % (test_no)
			out.write(x)
			break
		tmp = str(M)
		for i in tmp:
			if check[int(i)]==0:
				check[int(i)]=1
		if sum(check)==10:
			x = "Case #%d: %d\n" % (test_no, M)
			out.write(x)
			break
		count+=1
	test_no+=1
out.close()
print "saved in result.txt"
