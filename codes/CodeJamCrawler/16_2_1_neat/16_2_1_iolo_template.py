#!/usr/bin/python

import sys

def removeCharFromString(container,char):
	if container == char:
		return ""
	donde = container.index(char)
	if donde==0:
		return container[1:]
	if donde==len(container)-1:
		return container[0:len(container)-1]
	result = container[0:donde]+container[donde+1:]
	return result

def removeFromString(container,substr):
	result = container
	for carac in substr:
		result = removeCharFromString(result,carac)
	return result

def isContained(container,target):
	for car in target:
		if not car in container:
			return False
	return True

def isThree(container):
	if not isContained(container,"THR"):
		return False
	if container.count("E") < 2:
		return False
	return True

def isSeven(container):
	if not isContained(container,"SEVN"):
		return False
	if container.count("E") < 2:
		return False
	return True

def isNine(container):
	if not isContained(container,"NINE"):
		return False	
	if container.count("N") < 2:
		return False
	return True		

def solveRecursive(case,starting):
	if len(case)==0:
		return True,""
	if ("Z" in case) and (starting<=0):
		res,tlf = solveRecursive(removeFromString(case,"ZERO"),0)
		if res:
			return True,"0"+tlf
	if isContained(case,"ONE") and starting <=1:
		res,tlf = solveRecursive(removeFromString(case,"ONE"),1)
		if res:
			return True,"1"+tlf
	if isContained(case,"TWO") and starting <=2:
		res,tlf = solveRecursive(removeFromString(case,"TWO"),2)
		if res:
			return True,"2"+tlf
	if isThree(case) and starting <=3:
		res,tlf = solveRecursive(removeFromString(case,"THREE"),3)
		if res:
			return True,"3"+tlf
	if isContained(case,"FOUR") and starting <=4:
		res,tlf = solveRecursive(removeFromString(case,"FOUR"),4)
		if res:
			return True,"4"+tlf
	if isContained(case,"FIVE") and starting <=5:
		res,tlf = solveRecursive(removeFromString(case,"FIVE"),5)
		if res:
			return True,"5"+tlf
	if isContained(case,"SIX") and starting <=6:
		res,tlf = solveRecursive(removeFromString(case,"SIX"),6)
		if res:
			return True,"6"+tlf
	if isSeven(case) and starting <=7:
		res,tlf = solveRecursive(removeFromString(case,"SEVEN"),7)
		if res:
			return True,"7"+tlf
	if isContained(case,"EIGHT") and starting <=8:
		res,tlf = solveRecursive(removeFromString(case,"EIGHT"),8)
		if res:
			return True,"8"+tlf
	if isNine(case) and starting <=9:
		res,tlf = solveRecursive(removeFromString(case,"NINE"),9)
		if res:
			return True,"9"+tlf
	return False,""


def processCase(case):
	# *** BEGIN CODE PROCESSING CASE ***
	numbers = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
	res,resultado = solveRecursive(case.rstrip(),0)
	
	# *** END CODE PROCESSING CASE ***
	return resultado

def readCase(case):

	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()
		
	# *** END CODE READING CASE ***

	solution=processCase(caseInput)
	print "Case #"+str(case)+": "+solution

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

