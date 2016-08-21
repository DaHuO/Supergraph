#!/usr/bin/env python

class InputManager:
	def TextSplit(self,line,stri):
		s = stri.split('\n',line)
		result = list()
		for i in s:
			if i.count(' ')>0:
				x = i.split(' ',i.count(' '))
			else:
				x = i
			result.append(x)
		return result
	def convertInt(self,lists):
		result = list()
		for i in lists:
			if type(i) is str:
				result.append(int(i))
			elif type(i) is list:
				temp = list()
				for x in i:
					temp.append(int(x))
				result.append(temp)
		return result
	def concat(self,lists):
		st = ''
		for i in range(0,len(lists)):
			if i != len(lists)-1:
				st = st+str(lists[i])+'\n'
			else:
				st = st+str(lists[i])
		return st
	def splt(self,lists):
		result = list()
		for i in lists:
			x = i.count(' ')
			if x>0:
				y = i.split(' ',x)
			else:
				y = i
			result.append(y)
		return result

class FileManager:
	filename = 0
	def __init__(self,name):
		self.filename = name
	def openfile(self):
		f = open(self.filename,'r')
		strr = f.read()
		f.close()
		return strr
	def writefile(self,stri):
		f = open(self.filename,'w')
		f.write(stri)
		f.close()

fin = 'B-large.in'
fou = 'output_l'

input = InputManager()
fout = FileManager(fou)
intpt = list()
outpt = list()
with open(fin, "r") as ins:
    for line in ins:
    	line = line.rstrip()
        intpt.append(line)
number = intpt[0]
intpt.remove(number)

# print intpt
out = list()
for mem in intpt:
	found = ''
	isFound = False
	count = 0
	res = ''
	if len(mem) == 1:
		res = res+mem[0]

	else:
		for cha in mem:
			if not(isFound):
				isFound = True
				found = cha
				res = res+found
			else:
				if cha != found:
					res = res+cha
					found = cha


	out.append(res)

# print out

memcount = 1
outpt = list()
# caseCount = 'Case #'+str(memcount)+': '
for mem in out:
	caseCount = 'Case #'+str(memcount)+': '
	res = 0
	if len(mem)==1:
		if mem == '-':
			res = res+1
		outpt.append(caseCount+str(res))
	else:
		isFirst = True
		for i in mem:
			if isFirst:
				isFirst = False
				if i == '-':
					res = res + 1
			else:
				if i == '-':
					res = res + 2
		outpt.append(caseCount+str(res))
	memcount = memcount + 1

result = input.concat(outpt)
fout.writefile(result)


	# for cha in mem:
		# if !isFound:
		# 	found = cha
		# 	isFound = True
		#
		# if cha == found:
		# 	count = count+1
		#
		# elif ch != found:
		# 	res.append(found)
