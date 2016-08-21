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

fin = 'A-large.in'
fou = 'outputl'

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
intpt = input.convertInt(intpt)
count = 0
for mem in intpt:
	resultCount = 'Case #'+str(count+1) +': '
	f0 = False
	f1 = False
	f2 = False
	f3 = False
	f4 = False
	f5 = False
	f6 = False
	f7 = False
	f8 = False
	f9 = False
	init = 1
	if mem==0:
		outpt.append(resultCount+'INSOMNIA')
	else:
		while True:
			tmp = str(init*mem)
			for cha in tmp:
				if cha == '1':
					f1 = True
				elif  cha == '2':
					f2 = True
				elif  cha == '3':
					f3 = True
				elif  cha == '4':
					f4 = True
				elif  cha == '5':
					f5 = True
				elif  cha == '6':
					f6 = True
				elif  cha == '7':
					f7 = True
				elif  cha == '8':
					f8 = True
				elif  cha == '9':
					f9 = True
				elif  cha == '0':
					f0 = True
			if f1 and f2 and f3 and f4 and f5 and f6 and f7 and f8 and f9 and f0:
				outpt.append(resultCount+tmp)
				break
			init = init + 1
	count = count + 1
res = input.concat(outpt)
fout.writefile(res)
