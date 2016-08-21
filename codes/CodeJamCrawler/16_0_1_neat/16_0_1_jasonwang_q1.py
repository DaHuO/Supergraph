lst = []
countlist = []
filename = raw_input()
f = open(filename)
for line in f:
	lst.append(line.strip())
returnvalue = ''
lststr = ''

for i in range(1,int(lst[0])+1):
	if int(lst[i]) == 0:
		returnvalue = 'INSOMNIA'
		print 'Case #'+ str(i) + ':',returnvalue 
	else:
		lstnum = int(lst[i])
		lststr = lst[i]
		while True:
			for j in range(0,len(lststr)):
				if lststr[j] not in countlist:
					countlist.append(lststr[j]) 
				if len(countlist) == 10:
					returnvalue = lststr
					print 'Case #'+ str(i) + ':',returnvalue.strip()
					break
			lststr = str(int(lststr)+lstnum)
			if len(countlist) == 10:
				break
		countlist = []