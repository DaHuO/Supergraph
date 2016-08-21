# coding=utf-8


df = open('A-large.in').readlines()
case = int(df[0].strip())
df=df[1:]

for x in range(case):
	num = int(df[x].strip())
	if num == 0:
		print('Case #%d: INSOMNIA' % (x+1))
		continue
	numlist = set()
	for i in range(1,99999999999):
		finnum = num * i
		numlist = numlist | set(list(str(finnum)))
		if len(numlist) >= 10 :
			print('Case #%d: %d' % (x+1,finnum))
			break

