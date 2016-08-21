ifile = open('A-large.in')
ofile = open('large_output.txt', 'w')
t = int(ifile.readline())
arr = []
tcase = 1
for q in range(t):
	num = int(ifile.readline())
	arr.append(num)
for f in arr:
	li = ['0','1','2','3','4','5','6','7','8','9']
	count = 1
	d = f
	what = len(li)
	while len(li):
		d = f * count
		d1 = str(d)
		lis = list(d1)
		for x in lis:
			if x in li:
				li.remove(x)
		count = count + 1
		what = what - 1
		if count > pow(10, 6):
			d = "INSOMNIA"
			break
	out = "Case #%s: %s\n" %(tcase,d)
	ofile.write(out)
	tcase = tcase + 1

ifile.close()
ofile.close()