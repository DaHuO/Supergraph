#!/usr/bin/python
import sys

cases = int(sys.stdin.readline().rstrip("\n"),10)

num_b = {}
num_b[0]="ZERO" #Z
num_b[1]="ONE"             #O
num_b[2]="TWO" #W
num_b[3]="THREE"          #T
num_b[4]="FOUR" #U
num_b[5]="FIVE"		#F
num_b[6]="SIX" #X
num_b[7]="SEVEN"   	#S
num_b[8]="EIGHT" #G
num_b[9]="NINE" 	#

for c in range(0,cases):
	answer=[]
	answer1=""
	word=sys.stdin.readline().rstrip("\n")
	
	while True:
		if 'Z' in word:
			word=word.replace('Z','',1)
			word=word.replace('E','',1)
			word=word.replace('R','',1)
			word=word.replace('O','',1)
			answer.append(0)
		else:
			break

	while True:
		if 'W' in word:
			word=word.replace('T','',1)
			word=word.replace('W','',1)
			word=word.replace('O','',1)
			answer.append(2)
		else:
			break
	while True:
		if 'U' in word:
			word=word.replace('F','',1)
			word=word.replace('O','',1)
			word=word.replace('U','',1)
			word=word.replace('R','',1)
			answer.append(4)
		else:
			break
	while True:
		if 'X' in word:
			word=word.replace('S','',1)
			word=word.replace('I','',1)
			word=word.replace('X','',1)
			answer.append(6)
		else:
			break

	while True:
		if 'G' in word:
			word=word.replace('E','',1) # EIGHT
			word=word.replace('I','',1)
			word=word.replace('G','',1)
			word=word.replace('H','',1)
			word=word.replace('T','',1)
			answer.append(8)
		else:
			break

	while True:
		if 'O' in word:
			word=word.replace('O','',1) # ONE
			word=word.replace('N','',1)
			word=word.replace('E','',1)

			answer.append(1)
		else:
			break

	while True:
		if 'T' in word:
			word=word.replace('T','',1) # THREE
			word=word.replace('H','',1)
			word=word.replace('R','',1)
			word=word.replace('E','',1)
			word=word.replace('E','',1)
			answer.append(3)
		else:
			break

	while True:
		if 'F' in word:
			word=word.replace('F','',1) # FIVE
			word=word.replace('I','',1)
			word=word.replace('V','',1)
			word=word.replace('E','',1)
			answer.append(5)
		else:
			break

	while True:
		if 'S' in word:
			word=word.replace('S','',1) # 7
			word=word.replace('E','',1)
			word=word.replace('V','',1)
			word=word.replace('E','',1)
			word=word.replace('N','',1)
			answer.append(7)
		else:
			break

	while True:
		if 'I' in word:
			word=word.replace('N','',1) # 7
			word=word.replace('I','',1)
			word=word.replace('E','',1)
			word=word.replace('N','',1)
			answer.append(9)
		else:
			break



	
	answer.sort()
	for k in range(0,len(answer)):
		answer1=answer1+str(answer[k])
		

	print("Case #"+str(c+1)+": "+answer1)
