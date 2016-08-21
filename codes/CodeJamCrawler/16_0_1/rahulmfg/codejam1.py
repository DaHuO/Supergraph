#! usr/bin/python

f = open("A-large.in")

noc = int(f.readline())
case = 1
if noc <= 100:
	for no in f:
		checkList = []
		pickedNo = int(no)
		i = 1
		cpyNo = 0
		cpy2 = 0
		if pickedNo == 0:
			print "CASE #%d: INSOMNIA" % case
		else:
			while len(checkList) < 10:
				cpyNo = pickedNo * i
				cpy2 = cpyNo
				while cpyNo:
					tmp = cpyNo % 10
					if tmp not in checkList:
						checkList.append(tmp)
						if len(checkList) == 10:
							break
					cpyNo = cpyNo/10
				i += 1
			print "CASE #%d: %d" % (case, cpy2)
		case += 1