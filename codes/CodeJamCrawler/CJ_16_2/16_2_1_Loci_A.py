
cases = int(raw_input())

def isNumberInS(S,number):
	tmpS = S[:]
	for c in number:
		if c not in tmpS:
			return False
		else:
			tmpS.remove(c)
	return True

from random import shuffle

for case in range(cases):
	answer = []



	numberDict = {"SIX":6, "ONE":1, "TWO":2, "FOUR":4, "NINE":9, "FIVE":5, "ZERO":0, "THREE":3, "SEVEN":7, "EIGHT":8}
	numberArray = ["SIX", "ONE", "TWO", "FOUR", "NINE", "FIVE", "ZERO", "THREE", "SEVEN", "EIGHT"]
	S = raw_input()
	S = list(S)

	tmpS = ['foo']
	while len(tmpS) > 0:
		tmpS = S[:]
		shuffle(numberArray)
		answer = []
		
		for number in numberArray:
			while isNumberInS(tmpS,number):
				answer += [numberDict[number]]

				for c in number:
					#print S
					#print c
					tmpS.remove(c)
	if len(tmpS) > 0:
		print S
	answer.sort()
	answer = [str(i) for i in answer]
	print "Case #" + str(case+1) + ": " + ''.join(answer)
	#print S






