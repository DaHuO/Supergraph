#!/usr/bin/python
import sys
import binascii

#
def readFile(file):
	# lines(file)
	lines = [];
	for line in file:
		# print line
		lines.append(line)
	return lines;

def digitList():
	list = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
	# sortedList = []
	# for num in list:
	# 	sortedList.append(sorted(num))
	# return sortedList

def getNum(s):
	s = sorted(s)
	digitList = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
	rst = []
	helper(s, digitList, rst)
	rstStr = ""
	# print "rst:",rst
	for n in rst:
		rstStr += str(n)
	return rstStr

def helper(s, digitList, rst):
	# print "s:",s," rst:",rst
	if not s:
		# print "hey!",rst
		return True
	for i in range(0,10):
		num = digitList[i]
		# print "s:",s," num:",num
		tmp = ""
		hasNum = True
		for c in num:
			if c in s:
				# print c
				tmp = tmp + c
				s.remove(c)
				# print "now:",s
			else:
				# print "tmp:",tmp
				for ch in tmp:
					s.append(ch)
				s = sorted(s)
				# print "back:",s
				hasNum = False
				break;
		if(hasNum):
			rst.append(i)
			finished = helper(s, digitList, rst)
			if(finished):
				return True
			rst.pop()
			for ch in num:
				s.append(ch)
			s = sorted(s)
	return False





def main():
    file = open(sys.argv[1], "r+")
    rfile = open(sys.argv[2],'r+')
    print "file name: ", file.name
    lines = readFile(file)
    testNum = int(lines[0])
    print "testTotal:", testNum
    for i in range(1, testNum+1):
    	s = lines[i].rstrip()
    	r = getNum(s)
    	r = "Case #"+str(i)+": " + str(r)
    	rfile.write(r+"\n")
    	



if __name__ == '__main__':
    main()