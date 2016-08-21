'''
Google Code Jam 2016
Round 1B
Problem A -
'''

'''
ZERO - Z
TWO - W
FOUR - U
SIX - X
EIGHT - G

ONE - N, 3
THREE - R, 5
FIVE - V, 4
SEVEN - V, 5
NINE - N, 4
'''

import sys

sys.stdout
cases = int(raw_input())

for case in range (0, cases):
	data = raw_input().split(" ")
	for x in range (len(data)):
		data.extend(data[x])
	data.pop(0)
	
	y = []
	# 0, 2, 4, 6, 8
	for x in range (data.count("Z")):
		y.append(0)
		data.remove("Z")
		data.remove("E")
		data.remove("R")
		data.remove("O")
	for x in range (data.count("W")):
		y.append(2)
		data.remove("T")
		data.remove("W")
		data.remove("O")
	for x in range (data.count("U")):
		y.append(4)
		data.remove("F")
		data.remove("O")
		data.remove("U")
		data.remove("R")
	for x in range (data.count("X")):
		y.append(6)
		data.remove("S")
		data.remove("I")
		data.remove("X")
	for x in range (data.count("G")):
		y.append(8)
		data.remove("E")
		data.remove("I")
		data.remove("G")
		data.remove("H")
		data.remove("T")
	# 1
	for x in range (data.count("O")):
		y.append(1)
		data.remove("O")
		data.remove("N")
		data.remove("E")
	# 3
	for x in range (data.count("R")):
		y.append(3)
		data.remove("T")
		data.remove("H")
		data.remove("R")
		data.remove("E")
		data.remove("E")
	# 5
	for x in range (data.count("F")):
		y.append(5)
		data.remove("F")
		data.remove("I")
		data.remove("V")
		data.remove("E")
	# 7
	for x in range (data.count("S")):
		y.append(7)
		data.remove("S")
		data.remove("E")
		data.remove("V")
		data.remove("E")
		data.remove("N")
	# 9
	for x in range (data.count("I")):
		y.append(9)
		data.remove("N")
		data.remove("I")
		data.remove("N")
		data.remove("E")
	
	y.sort()
	
	number = ""
	for x in range (len(y)):
		number = number + str(y[x])
	
	print ("Case #{}: {}".format(case + 1, number))