#!/usr/bin/env python





t=int(input(''))
for i in range(t):
	str_inp=str(input(""))
	t=[] #- + - + +
	for x in str_inp:
		t.append(x)
		pass

	count=0
	temp=[]
	def i_bool(x):
		for i in x:
			if i != "+":
				return True
				pass
			pass
		return False

		pass
	while i_bool(t):
		tem=t.pop(0)
		temp.append(tem)
		if len(t)> 0:
			while tem == t[0] :
				temp.append(t.pop(0))
				if len(t) == 0:
					break
					pass
				pass
			pass
		pass
		for x in temp:
			if x == '-':
				t.insert(0,'+')
				pass
			else:
				t.insert(0,'-')
				pass
			pass
		temp=[]
		count+=1
	print("Case #{0}: {1}".format(i+1,count))
	pass