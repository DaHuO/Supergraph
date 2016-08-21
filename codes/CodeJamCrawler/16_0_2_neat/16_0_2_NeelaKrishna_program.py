

def digitize(N):
	digits=[]
	for i in list(str(N)):
		i=int(i)
		if i not in digits:
			digits.append(i)
	return digits

def flip():
	pass

from collections import Counter
from itertools import groupby

def consecutivetopscenario(group):
	print group
	side=0
	for i,v in enumerate(group[::-1]):
		print i,v
		if group[-1] == v:
			side=side+1
		else:
			break
	counterside=0
	print group[:-1*(i)]
	for j,v in enumerate(group[:-1*(i)][::-1]):
		print j,v
		if group[-1] != v:
			counterside=counterside+1
		else:
			break
	return {group[-1]:side,group[-1*(i+1)]:counterside}

from itertools import permutations,product
from collections import deque

def flip(lst,I):
	for i in range(I):
		if lst[i] == '-':
			lst[i] = '+'
		else:
			lst[i]= '-'
	return lst[:I][::-1]+lst[I:]

def doit(pancakes):
	print "Got",pancakes
	if pancakes == ['-']:
		print "Flipped "+str(['+'])
		print "All happy"
		print "---------"
		return 1
	elif pancakes == ['+']:
		print "All happy"
		print "---------"
		return 0
	# Search for tail + and reduce the problem
	try:
		I=len(pancakes)-pancakes[::-1].index('-')
		if I < len(pancakes) and I >0:
			pancakes=pancakes[:I]
			print "Reduced the group "+str(pancakes)
	except Exception as inst:
		print inst,"When tried to reduce"
		print "All happy"
		print "---------"
		return 0


	# Flip the first n + 	
	I = pancakes.index('-')
	if I > 0:
		for i in range(I):
			pancakes[i]='-'
		print "Flipped first ",I,str(pancakes)
		return doit(pancakes)+1

	# flip all the group
	pancakes=flip(pancakes,len(pancakes))
	print "Flipped all group "+str(pancakes)
	return doit(pancakes)+1
	# try:
	# except Exception as inst:
	# 	print inst
	# 	for i in range(len(pancakes)):
	# 		pancakes[i]='+'
	# 	print "Flipped "+str(pancakes)
	# 	print "All happy"
	# 	print "---------"
	# 	return 1
	# # 	return 0
	# # for i,v in enumerate(pancakes):
	# # 	if pancakes[i]
	# # 	newgroup[i]=pancakes
	# # if pancakes[-1] != '-':
	# # 	for i in range(1,len(pancakes)):
	# # 		if pancakes[-1*i] == '-':
	# # 			I=len(pancakes)-i
	# # 			break
	# # 	print "All happy"
	# # 	print "---------"
	# # 	return 0
	# # newgroup=list(pancakes[:I+1])
	# print "Reduced to first "+str(I+1)+" "+str(newgroup)
	# J=newgroup.index('-')-1
	# if J==-1:
	# 	print "All happy"
	# 	print "---------"
	# 	return 0
	# if J>=0:
	# 	for i in range(J+1):
	# 		newgroup[i]='-'
	# 	print "Flipped first "+str(J+1)+str(newgroup)
	# 	return doit(newgroup)+1

	# for i,v in enumerate(newgroup[::-1]):
	# 	# print i,v
	# 	if v == '+':
	# 		newgroup[i]='-'
	# 	else:
	# 		newgroup[i]='+'
	# print "newgroup",newgroup
	# if newgroup == pancakes:
	# 	print "Aha!"
	# 	quit()
	# print "---"
	# return doit(newgroup)+1
	# # if results['+'] > results['-'] and group[-1]=='-':
	# 	# flip(group)

	# # print Counter(pancakes)


fo=open("output.out","w")
f=open("B-large.in","r")
inp=f.read()
# print inp
f.close()
inp=inp.split('\n')
T=int(inp[0])
inp=inp[1:]
for x in range(T):
	fo.write("Case #"+str(x+1)+": "+str(doit(list(inp[x])))+"\n")
fo.close()