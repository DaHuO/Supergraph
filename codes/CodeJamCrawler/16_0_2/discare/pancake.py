# coding=utf-8


df = open('B-large.in').readlines()
case = int(df[0].strip())

df=df[1:]

def flipped(list1):
	if len(list1) == 0:
		return True
	for x in list1:
		if x == '-':
			return False
	return True

def flipall(list2):
	for x in range(len(list2)):
		if list2[x] == '+' :
			list2[x] = '-'
		else:
			list2[x] = '+'

def flipcake(clist):
	if flipped(clist):
		return 0
	if clist[-1] == '+':
		return flipcake(clist[:-1])
	else:
		flipall(clist)
		return 1 + flipcake(clist[:-1])

for x in range(case):
	clist = list(df[x].strip())
	print('Case #%d: %d' % (x+1,flipcake(clist)))

