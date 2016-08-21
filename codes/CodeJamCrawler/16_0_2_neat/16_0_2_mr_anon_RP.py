def flip(myList,i,j):
	temp = list(myList)
	temp2 = j
	temp3 = i
	while(temp2 >= i):
		if temp[temp2] == '-':
			myList[temp3] = '+'
		else:
			myList[temp3] = '-'
		temp3 = temp3 + 1
		temp2 = temp2 - 1
	return myList

def check(myList):
	for i in myList:
		if i == '-':
			return 0
	return 1

t = input()
for case in range(0,t):
	text = str(raw_input())
	S = list(text)
	length = len(S) - 1
	steps = 0
	while length >= 0 and check(S) == 0:
		if S[length] == '-':
			steps = steps + 1
			if S[0] == '+':
				j = 1
				while S[j] == '+' and j < len(S):
					j = j+1
				S = flip(S,0,j-1)
				steps = steps + 1
				S = flip(S,0,length)
			else:
				flip(S,0,length)
		length = length - 1
	print "Case #%d: %d"%(case+1,steps)
