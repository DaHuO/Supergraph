import itertools
tcases=int(input())
case=1

def last_word(string):
	if string=='':
		print()
		return
	a=[string[0]]
	temp=[]
	for e in string[1:]:
		temp=[]
		i=0
		while i<len(a):
			temp.append(a[i]+e)
			temp.append(e+a[i])
			i+=1
		a=temp[:]
	a.sort()
	print(a[-1])
while case<=tcases:
	print('Case #'+str(case)+':',end=' ')
	last_word(input())
	case+=1