f = open("A-large.in", "r")
fo = open("output.txt","w")

count = int(f.readline())

for case in xrange(0,count):
	print case
	num_num = int(f.readline())
	if num_num == 0:
		fo.write("Case #"+str(case+1)+": "+"INSOMNIA"+"\n")
		continue
	dict_num = {}
	count = 0
	wohoo = True
	mult_num = 1
	new_num = 0
	templist = []
	for x in xrange(0,10):
		dict_num[str(x)] = 0

	while wohoo:
		new_num = mult_num * num_num
		str_num = str(new_num)
		for x in xrange(0,len(str_num)):
			dict_num[str_num[x]] += 1
		for x in xrange(0,10):
			templist.append(dict_num[str(x)])
		if (0 not in templist):
			wohoo = False
			break
		mult_num +=1
		templist = []
	fo.write("Case #"+str(case+1)+": "+str(new_num)+"\n")