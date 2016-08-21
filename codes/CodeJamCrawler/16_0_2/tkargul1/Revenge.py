#!/usr/bin/env python
__author__ = "Thomas Kargul"

def revenge():
	numOfInput = int(raw_input()) # 1 <= T <= 100
	inputS = [] #list of strings
	for i in range(numOfInput):
		inp = raw_input()
		inputS.append(inp)

	#flipping = reversing a string, and "inverse"
	def flip(pancakes):
		pancakes.reverse()
		for i, p in enumerate(pancakes):
		 	pancakes[i] = "+" if p == "-" else "-"
		#flipCount += 1
		return pancakes

	#find how many + are at the end of the string,
	#since they are already +, don't flip these
	#flip goes from [0]->index before first + in the last consecutive group of +
	def findBackCount(S):
		backCount = len(S)
		for i, sign in reversed(list(enumerate(S))):
			if sign == "+":
				backCount = i
			else:
				break
		return backCount #index of first rear set of +

	#find the number of + in beginning, these will be flipped to -
	#before the bigger flip, so after they bigger flip they will
	#be on bottom and be + again
	def findFrontPlus(S):
		frontPlus = 0
		if S[0] == "+":
			for sign in S:
				if sign == "+": frontPlus += 1
				else: break
		return frontPlus


	#if no -, then all pancakes are flipped to + aka happy side
	def allHappy(S):
		for sign in S:
			if sign == "-": return False
		return True

	for case, strS in enumerate(inputS):
		S = list(strS)
		flipCount = 0 #reset for each S in inputs

		while not allHappy(S):
			backCount = findBackCount(S) 
			frontPlus = findFrontPlus(S)
			if frontPlus > 0:
				#flip front +'s to -'s before the bigger flip
				frontS = S[0:frontPlus:]
				backS = S[frontPlus::]
				frontS_flipped = flip(frontS)
				flipCount += 1
				S = frontS_flipped + backS
			#bigger flip
			if backCount < len(S):
				frontS = S[0:backCount:]
				backS = S[backCount::]
				frontS_flipped = flip(frontS)
				flipCount += 1
				S = frontS_flipped + backS
			else:
				#there are no + at the back
				S = flip(S)
				flipCount += 1

		print("Case #{}: {}".format(case+1, flipCount))

	#go as far down the stack until EOS or only "+"s left
		#if + on top*** and - on bottom, flip top first so that it becomes - 
			#and thus becomes a + when the stack is flipped
			#i.e +++-- > -++-- > ++--+
		#*** or flip entire consecutive +'s on top so they become -'s before flip, then +'s again after flip

	#find pancakes to be flipped then 
	#send S[0:end_of_flip: ] to flip()
	#return of flip().append( S[end_of_flip:len(S): ] )



if __name__ == '__main__':
	revenge()