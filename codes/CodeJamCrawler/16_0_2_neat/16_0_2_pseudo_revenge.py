import sys
import time

inputfile=open(sys.argv[1],'r')
outputfile = open(sys.argv[1].replace("in","out"),'w')

testcases = int(inputfile.readline())

for i in range(0, testcases):
		stack = inputfile.readline()
		flips = 0
		while "-" in stack:
				index = stack.rfind("-")
				stack = stack[:index+1].replace("-","|") + stack[index+1:]
				stack = stack[:index+1].replace("+","-") + stack[index+1:]
				stack = stack[:index+1].replace("|","+") + stack[index+1:]
				flips = flips + 1
				#print stack
				#print flips
				#time.sleep(2) 
		outputfile.write("Case #" + str(i+1) + ": " + str(flips) + "\n")
outputfile.close()
