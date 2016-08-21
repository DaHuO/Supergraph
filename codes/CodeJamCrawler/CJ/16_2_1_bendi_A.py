numberNames = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def toNum(letter):
	return(ord(letter)-ord('A'))

letterOrder="ZWXUORFSHI"

solveByLetter = {toNum('Z'):0,toNum('W'):2,toNum('X'):6,toNum('U'):4,toNum('O'):1,toNum('R'):3,toNum('F'):5,toNum('S'):7,toNum('H'):8,toNum('I'):9}


for case in range(1, int(input())+1):
	S = input()
	freqs = []
	for i in range(26):
		freqs.append(S.count(chr(ord('A')+i)))
	result=""
	for test in letterOrder:
		x = freqs[toNum(test)]
		currNumber = solveByLetter[toNum(test)]
		#I have x times currNumber
		result += chr(ord('0')+currNumber) * x
		for l in numberNames[currNumber]:
			p = toNum(l)
			freqs[p] -= x

	print ("Case #%d: %s" % (case,"".join(sorted(list(result)))))

