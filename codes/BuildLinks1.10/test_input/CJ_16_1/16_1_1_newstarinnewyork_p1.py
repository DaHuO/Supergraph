fi = open("input","r")
fo = open("output","w")
t = int(fi.readline())

for i in range(t):
	quiz = fi.readline()
	winning = quiz[0]
	for j in range(1,len(quiz)):
		if winning[0] > quiz[j]:
			winning = winning + quiz[j]
		else:
			winning = quiz[j] + winning  	

	fo.write("Case #{0}: {1}".format(i+1,winning))
fi.close()
fo.close()