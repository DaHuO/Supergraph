def StringLength(n,char):
	to_return = ''
	for i in range(n):
		to_return = to_return+char
	return to_return

def flip(string):
	if string=="":
		return ""
	elif string[0]=='+':
		# global count
		# count+=1
		return StringLength(len(string),'-')
	elif string[0]=='-':
		# # global count
		# count+=1
		return StringLength(len(string),'+')



def bothIndicesOfNext_GroupFromLeft(string):
	_found = False
	start = 0
	for i in range(len(string)):
		if string[i]=='+' and _found:
			return [start,i]
		elif string[i]=='-' and _found==False:
			start = i
			_found = True
	if not _found:
		return [-1,-1]
	else:
		return [start, len(string)-1]

# print bothIndicesOfNext_GroupFromLeft("+++++")
# [2,4]

def doIt(st):
	print "got:",st
	[start,final] = bothIndicesOfNext_GroupFromLeft(st)
	if (start!=-1 or final!=-1):
		if start==0:
			global count
			count+=1
			doIt(StringLength(final-start,'+')+st[final:len(st)])
		elif (start==len(st)-1 and final==len(st)-1):
			count+=2
			doIt(StringLength(len(st),'+'))
		else:
			count+=2
			doIt(StringLength(final,'+')+st[final:len(st)])
	else:
		return


myset = set('')
ifile = open('B-large.in','r')
ofile = open('output.txt','w')

total = 0
total = int(ifile.readline())

for i in range(total):
	count = 0
	string = ifile.readline()
	doIt(string)
	ofile.write("Case #"+str(i+1)+": "+str(count)+"\n")

ifile.close()
ofile.close()
	# result = bothIndicesOfNext_GroupFromLeft(st)
	# if result==[0,0]:
	# 	return st
	# else:
	# 	start = result[0]
	# 	final = result[1]
	# 	print "start:",start
	# 	print "final:",final
	# 	corrected = flip(flip(st[0:start]) +st[start:final])
	# 	return doIt(corrected+st[final:len(st)])


# string = "--+-"
# print doIt(string)
# print count

	# if string[0]=='+':
	# 	index = 0
	# 	while index!=len(string):
	# 		if string[index]=='+':
	# 			index+=1
	# 		else:
	# 			break
	# 	return [string[0:index],string[index:(len(string))]]
	# else:
	# 	index = 0
	# 	while index!=len(string):
	# 		if string[index]=='-':
	# 			index+=1
	# 		else:
	# 			break
	# 	return [string[0:index],string[index:(len(string))]]

# print n



# print nextGroupFromLeft(string)
# print flipAtIndex("---++",indexOfRightMost_("---++"))