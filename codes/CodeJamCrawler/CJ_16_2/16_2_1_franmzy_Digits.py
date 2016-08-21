# -*- coding: utf-8 -*-
######################################################
##                                                  ##
##  Fran Muñoz                                      ##
##  email: fran.mzy@gmail.com                       ##
##  UVA user: franmzy                               ##
##  Linkedin: https://www.linkedin.com/in/franmzy   ##
##                                                  ##
######################################################

numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def isEnought( str ):
	auxd = {}
	for c in str:
		if c in auxd:
			auxd[c] += 1
		else:
			auxd[c] = 1

	for k in auxd:
		if k not in tndict:
			return False
		if auxd[k] > tndict[k]:
			return False
	return True

def removeNum( str ):
	for c in str:
		tndict[c] -= 1

def addNum( str ):
	for c in str:
		tndict[c] += 1



def backtrack( n ):
	if n == 0:
		return True

	for i in range(len(numbers)):
		if isEnought(numbers[i]):
			removeNum(numbers[i])
			if backtrack( n - len(numbers[i])):
				sol.append(i)
				return True
			addNum(numbers[i])






n_cases = int(input())
for i_case in range(n_cases):
    
    tn = input()
    tndict = {}
    sol = []
    for l in tn:
    	if l in tndict:
    		tndict[l] += 1
    	else:
    		tndict[l] = 1

    backtrack(len(tn))

    print('Case #{0}:'.format(i_case+1), end=" ")

    print( "".join(list(map(str, sol[::-1]))))