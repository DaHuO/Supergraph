#!/usr/bin/python
import sys
import binascii


def readFile(file):
	# lines(file)
	lines = [];
	for line in file:
		# print line
		lines.append(line)
	return lines;

def count(N):
	n = int(N)
	num = n
	ary = []
	list = [False]*10
	cnt = 0
	multiple = 1;
	while((num not in ary) and cnt < 10):
		num = multiple * n
		if(num <= 0):
			return "INSOMNIA"
		while(num > 0):
			curr = num % 10
			if(list[curr] == False):
				list[curr] = True
				cnt += 1
			if(cnt == 10):
				return multiple * n
			num /= 10
		multiple += 1

	return "INSOMNIA"




def main():
    file = open(sys.argv[1], "r+")
    rfile = open(sys.argv[2],'r+')
    print "file name: ", file.name
    lines = readFile(file)
    testNum = int(lines[0])
    print "testTotal:", testNum
    for i in range(1, testNum+1):
    	r = count(lines[i])
    	r = "Case #"+str(i)+": "+str(r)
    	# print r
    	rfile.write(r+"\n")



if __name__ == '__main__':
    main()