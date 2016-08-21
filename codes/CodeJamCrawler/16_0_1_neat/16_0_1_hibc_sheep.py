f = open ('A-large.in.txt', 'r')
fw = open('output2.txt','w')
T = int(f.readline())
#print T

for i in range (1, T+1):
	N = int(f.readline())
	lst = []
	for j in range (1,200+1):

		if (N == 0):
			break;

		rst = N * j
		if (rst >= 10):
			lst.extend(map(int,str(rst)))
		else:
			lst.append(rst)

		if (len(set(lst)) == 10):
			break
		else:
			continue
	if (len(lst) < 10):
		print >> fw, "Case #%d: INSOMNIA" % (i)
	else:
		print >> fw, "Case #%d: %d" % (i,rst)
		#print lst
f.close()
fw.close()