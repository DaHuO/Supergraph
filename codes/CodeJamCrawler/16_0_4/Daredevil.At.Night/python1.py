a = int(raw_input())
for i in range(a):
	list1 = raw_input().split(" ")
	k = int(list1[0])
	c = int(list1[1])
	s = int(list1[2])
	listAns = []
	for j in range(1,k+1):
		listAns.append(str(j))
	print ("Case #" + str(i+1)+": " + ' '.join(listAns))
