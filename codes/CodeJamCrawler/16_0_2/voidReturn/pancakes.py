import sys

def main():

	filename = sys.argv[-1]

	r_file = open(filename, "r")
	w_file = open("Boutput.txt", "w")
	T = int(r_file.readline())

	if T >= 1 and T <= 100:
		for cases in range(T):

			p = list((r_file.readline().rstrip()))
			S = len(p)
			
			if isFormatted(p) and S >= 0 and S <= 100:
				print("Original %s \n" %p)
				flips =0
				while p.count('+') is not len(p):
					#temp = list(p)
					
					index = findIndexToFlip(p)
					p = list(flipPancake(int(index), p, flips))

					#if areListsEqual(temp, p):
						#print("\tTHey are eqal")
					#	temp = fixLoop(p, flips)

					#p = list(temp)
	
					flips +=1
					

				print("\nCase #%s: %s" %((cases+1), flips))
				w_file.write("Case #%s: %s \n" %((cases+1), flips))
			



def flipPancake(theIndex, pancake, flips):


	myTemp = list(pancake)
	for status in range(theIndex+1):
		if pancake[status] == '+':
			pancake[status]= '-'
		else:
			pancake[status]= '+'

	#print("\n\tFlips  index: %s to : %s  " %(theIndex, pancake))
	pancake[:(theIndex+1)] = pancake[:(theIndex+1)][::-1]
	

	#print("\tReverse: %s " %pancake)

	#if flips > 0 and (areListsEqual(myTemp, pancake) or (pancake.count('+') == len(pancake)-1 and containsPattern(pancake))) :
		#print("\tgello")
		#return myTemp

	return pancake


def findIndexToFlip(pancake):
	index = 0


	if pancake[index] == "+" and len(pancake) >= 2:
		while pancake[index+1] == "+":
			index += 1
		#print("\t GOt the plus %s" %index)
		return index


	for i in range(len(pancake)-1):
		if pancake[i+1] == '-':
			index = i+1

	#print("\tFound at: %s" %index)
	return index


def isFormatted(arr):
	return arr.count("+") + arr.count("-") == len(arr)

def fixLoop(pancake, flips):
	iterate = len(pancake)-1

	position = None
	while iterate >= 1:
		if pancake[iterate] == '-' and pancake[iterate-1] == '+':
		#	print("Fixed index: %s" %(iterate-1))
			position = iterate		
		#	print("\n\t Give me : %s" %pancake)
			
		iterate-=1
	if position != None:
		pancake = flipPancake((position-1), pancake, flips)
		return pancake

def areListsEqual(l1, l2):
	size = len(l1)
	for i in range(size):
		if l1[i] != l2[i]:	
			return False

	return True

def containsPattern(checkList):
	size = len(checkList)

	amount = 0
	for i in range(size-1):
		if(checkList[i] == "+" and checkList[i+1] == "-"):
			amount += 1
	
	if amount == 1:
		return True

	return False

main()		

