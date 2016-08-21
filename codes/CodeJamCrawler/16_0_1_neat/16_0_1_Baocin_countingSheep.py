#!/bin/python3.5


#Author: Michael Pedersen

import sys

with open( sys.argv[1] ) as file_input:
	totalNumCases = int(file_input.readline())
	for case in range(0,totalNumCases):
		num = int(file_input.readline())
		#print(num)
		out = "NULL";
		if num == 0:
			out = "INSOMNIA"
		else:
			seen = set()
			multipler = 1
			running = True
			while running:
				newNum = multipler * num
				newString = str(newNum)
				#print("runnings", multipler, newNum, newString, seen)
				for char in newString:
					seen.add(char)
				if len(seen) == 10:
					#print("Done", multipler, newNum, newString, seen)
					out = newNum
					running = False
					break;
				multipler+=1
					
		print("Case #"+str(case+1)+":", out)
			
			
