import sys, os

infile = r'c:\cj2016\largein.txt'

inf = open(infile,'r')
otf = open(r'c:\cj2016\out.txt','w')

nocase = int(inf.readline())


for i in range(1,nocase+1):
	num = int(inf.readline())
	notfound = ['0','1','2','3','4','5','6','7','8','9']

	if num == 0:
		otf.write('Case #' + str(i) + ': INSOMNIA\n')
		continue
	else:
		N = 0
		print 'case ' + str(i)
		print 'num ' + str(num)
		while(True):
			N += 1
			cnum = N * num
			print 'cnum ' + str(cnum)
			for c in str(cnum):
				print c
				try:
					print 'removed ' + c
					notfound.remove(c)
				except:
					pass
	
			if len(notfound) == 0:
				break

		otf.write('Case #' + str(i) + ': ' + str(cnum) + '\n')

inf.close()
otf.close()