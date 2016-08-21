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

#if prime return -1, else return some divsor
def isPrime(n):
	if n <= 3:
		return -1
	elif n % 2 == 0:
		return 2
	elif n % 3 == 0:
		return 3
	i = 5
	while i * i <= n:
		if n % i == 0:
			return i
		if n % (i + 2) == 0:
			return i + 2
		i += 6
	return -1

def ifAllNotPrime(s):
	list = s + " "
	for i in range(2, 11):
		n = int(str(int(s, i)),10)
		#print "base ",i,": ",n
		div = isPrime(n)
		if(div == -1):
			return None
		list = list + " " + str(div)
	#print "list:",list
	return list

def findJcoins(N, J):
	rst = []
	cnt = 0
	start = "".ljust(N-2,'0')
	end = "".ljust(N-2,'1')
	s = start
	n = int(s,2)
	while(n <= int(end,2) and cnt < J):
		bstr = bin(n)[2:]
		bstr = bstr.rjust(N-2,'0')
		s1 = "1" + bstr + "1"
		r = ifAllNotPrime(s1)
		if(r != None):
			rst.append(r)
			cnt += 1
		n = n + 1
	return rst





def main():
    file = open(sys.argv[1], "r+")
    rfile = open(sys.argv[2],'r+')
    print "file name: ", file.name
    lines = readFile(file)
    testNum = int(lines[0])
    print "testTotal:", testNum
    for i in range(1, testNum+1):
    	nums = lines[i].split()
    	N = int(nums[0])
    	J = int(nums[1])
    	rlist = findJcoins(N, J)
    	r = "Case #"+str(i)+":"
    	rfile.write(r+"\n")
    	for i in range(0,J):
    		rfile.write(rlist[i]+"\n")

# if(n == 2 or n == 3):
# 		return -1
# 	if(n % 2 == 0):
# 		return 2
# 	for i in range(3,int(n**0.5)+1,2):
# 		if n % i == 0:
# 			return i

# 	return -1

if __name__ == '__main__':
    main()