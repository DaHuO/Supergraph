from __future__ import print_function
import fileinput
from sets import Set

f = fileinput.input()

T = int(f.readline())
for case in range(1,T+1):
	letters=f.readline().rstrip()
	letters=list(letters)
	result=list()
	while "Z" in letters:
		letters.remove("Z")
		letters.remove("E")
		letters.remove("R")
		letters.remove("O")
		result.append(0)
	while "W" in letters:
		letters.remove("T")
		letters.remove("W")
		letters.remove("O")
		result.append(2)
	while "X" in letters:
		letters.remove("S")
		letters.remove("I")
		letters.remove("X")
		result.append(6)
	while "U" in letters:
		letters.remove("F")
		letters.remove("O")
		letters.remove("U")
		letters.remove("R")
		result.append(4)
	while "O" in letters:
		letters.remove("O")
		letters.remove("N")
		letters.remove("E")
		result.append(1)
	while "F" in letters:
		letters.remove("F")
		letters.remove("I")
		letters.remove("V")
		letters.remove("E")
		result.append(5)
	while "S" in letters:
		letters.remove("S")
		letters.remove("E")
		letters.remove("V")
		letters.remove("E")
		letters.remove("N")
		result.append(7)
	while "R" in letters:
		letters.remove("T")
		letters.remove("H")
		letters.remove("R")
		letters.remove("E")
		letters.remove("E")
		result.append(3)
	while "G" in letters:
		letters.remove("E")
		letters.remove("I")
		letters.remove("G")
		letters.remove("H")
		letters.remove("T")
		result.append(8)
	while letters:
		letters.remove("N")
		letters.remove("I")
		letters.remove("N")
		letters.remove("E")
		result.append(9)
	result.sort()
	result=[str(i) for i in result]
	result="".join(result)
	print("Case #"+str(case)+": "+result)
