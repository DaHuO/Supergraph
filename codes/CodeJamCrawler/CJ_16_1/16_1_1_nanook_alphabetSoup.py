'''
Problem

On the game show The Last Word, the host begins a round by showing the contestant a string S of uppercase English letters. The contestant has a whiteboard which is initially blank. The host will then present the contestant with the letters of S, one by one, in the order in which they appear in S. When the host presents the first letter, the contestant writes it on the whiteboard; this counts as the first word in the game (even though it is only one letter long). After that, each time the host presents a letter, the contestant must write it at the beginning or the end of the word on the whiteboard before the host moves on to the next letter (or to the end of the game, if there are no more letters).

For example, for S = CAB, after writing the word C on the whiteboard, the contestant could make one of the following four sets of choices:

put the A before C to form AC, then put the B before AC to form BAC
put the A before C to form AC, then put the B after AC to form ACB
put the A after C to form CA, then put the B before CA to form BCA
put the A after C to form CA, then put the B after CA to form CAB
The word is called the last word when the contestant finishes writing all of the letters from S, under the given rules. The contestant wins the game if their last word is the last of an alphabetically sorted list of all of the possible last words that could have been produced. For the example above, the winning last word is CAB (which happens to be the same as the original word). For a game with S = JAM, the winning last word is MJA.

You are the next contestant on this show, and the host has just showed you the string S. What's the winning last word that you should produce?

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the winning last word, as described in the statement.

Limits

1 ≤ T ≤ 100.
Small dataset

1 ≤ length of S ≤ 15.
Large dataset

1 ≤ length of S ≤ 1000.
Sample


Input 
 	
Output 
 
7
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE

Case #1: CAB
Case #2: MJA
Case #3: OCDE
Case #4: BBAAA
Case #5: CCCABBBAB
Case #6: CCCBAABAB
Case #7: ZXCASDQWE


'''
import math
import copy


def wordBuilder(inputLine):
	wordList = list(inputLine)
	position = len(wordList) - 1
	#startPoint = math.floor(position/2)
	builtWords = [[""] * ((position + 1) * 2)]
	#shift = 0
	
	for wordIndex in range(len(wordList)): 
				
		if wordIndex is 0:
			
			builtWords[0][position] = wordList[wordIndex]
			newBuiltWords = builtWords
			#print (wordIndex, ":", builtWords)
		
		else:
			#print (wordIndex, ":", builtWords)
			tempBuiltWords1 = copy.deepcopy(builtWords)
			tempBuiltWords2 = copy.deepcopy(builtWords)
			#shift += 1
			
			newBuiltWords = []
			
			for baseAlphabet1 in tempBuiltWords1:
				baseAlphabet1[(position + wordIndex)] = wordList[wordIndex]
				newBuiltWords.append(baseAlphabet1)

			for baseAlphabet2 in tempBuiltWords2:
				baseAlphabet2[(position - wordIndex)] = wordList[wordIndex]
				newBuiltWords.append(baseAlphabet2)				
			
			#print (builtWords, "\n", tempBuiltWords2)
			#newBuiltWords = builtWords + tempBuiltWords2
			#print (newBuiltWords)



		builtWords = newBuiltWords
	

	finalWords = ["".join(word) for word in builtWords ]
	finalWords.sort()
	return (finalWords[-1])


	#print (builtWords)





	



def googleCodeReporter():
	inputFileName = "2016_A_small_attempt0.in"
	outputFileName = inputFileName[:-3] + ".out"
	print (outputFileName)

	listOut = []
	with open(inputFileName) as inputFile:
		inputFile = list(inputFile)
		sampleSize = int(inputFile[0])
		sampleIndex = range(1,sampleSize+1)

		for x in sampleIndex:
			inputFile[x] = inputFile[x].rstrip()
			value = wordBuilder(inputFile[x])
			listOut.append(''.join(["Case #",str(x),": ", str(value)]))



	with open(outputFileName, 'w') as outputFile:
		for item in listOut:
			outputFile.write("%s\n" % item)

googleCodeReporter()