'''Problem

You just made a new friend at an international puzzle conference, and you asked for a way to keep in touch. 
You found the following note slipped under your hotel room door the next day:

"Salutations, new friend! 
I have replaced every digit of my phone number with its spelled-out uppercase 
English representation ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" for the digits 0 through 9, in that order), and then reordered all of those letters in some way to produce a string S. It's up to you to use S to figure out how many digits are in my phone number and what those digits are, but I will tell you that my phone number consists of those digits in nondecreasing order. Give me a call... if you can!"

"ZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINE"

You would to like to call your friend to tell him that this is an obnoxious way to give someone a phone number, but you need the phone number to do that! What is it?

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S of uppercase English letters.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is a string of digits: the phone number.

Limits

1 ≤ T ≤ 100.
A unique answer is guaranteed to exist.
Small dataset

3 ≤ length of S ≤ 20.

Large dataset

3 ≤ length of S ≤ 2000.

Sample


Input 
 	
Output 
 
4
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER

Case #1: 012
Case #2: 2468
Case #3: 114
Case #4: 3

"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
"ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"				zERO
"ONE", "TWO", "THREE", "FOUR", "FIVE", "SEVEN", "EIGHT", "NINE"						SIx
"ONE", "TWO", "THREE", "FOUR", "FIVE", "EIGHT", "NINE"								SEvEN
"ONE", "THREE", "FOUR", "FIVE", "EIGHT", "NINE"										TwO
"ONE", "THREE", "FOUR", "EIGHT", "NINE"												FIvE
"ONE", "THREE", "FOUR", "NINE"														EIgHT
"ONE", "FOUR", "NINE"																"ThREE"
"ONE", "NINE"																		"FOuR"
"NINE"																				"oNE"
					NINE


"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
"ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"				zERO
"ONE", "TWO", "THREE", "FOUR", "FIVE", "SEVEN", "EIGHT", "NINE"						SIx
"ONE", "THREE", "FOUR", "FIVE", SEvEN, "EIGHT", "NINE"								TwO
"ONE", "THREE", "FOUR", "FIVE", SEvEN, "NINE"								eiGht
"ONE", "THREE", "FIVE", SEvEN, "NINE"								foUr
"ONE", "THREE", "FIVE", "NINE"								sEVEN
			six
			two
			eight
			foUR
			seven
			FIVE
			Nine
			Three
			one


											FIvE
			EIgHT
"ONE", "FOUR", "NINE"																"ThREE"
"ONE", "NINE"																		"FOuR"
"NINE"																				"oNE"
					NINE


'''
import jam


def solve(case):
	numberOut = list()
	letterCountDict = {'S':0, 'R':0, 'O':0, 'U':0, 'W':0, 'T':0, 'N':0, 'V':0, 'G':0, 'H':0, 'I':0, 'E':0, 'F':0, 'X':0, 'Z':0}
	listLetters = list(case.readLine())
	for x in listLetters:
		letterCountDict[x] += 1

	#print (letterCountDict)

	#remove zeros
	while letterCountDict['Z'] != 0:
		numberToRemove = letterCountDict['Z']
		numberOut.extend([0]*numberToRemove)

		letterCountDict['E'] -= numberToRemove
		letterCountDict['R'] -= numberToRemove
		letterCountDict['O'] -= numberToRemove
		letterCountDict['Z'] -= numberToRemove
		

	while letterCountDict['X'] != 0:
		numberToRemove = letterCountDict['X']
		numberOut.extend([6]*numberToRemove)
		
		letterCountDict['I'] -= numberToRemove
		letterCountDict['S'] -= numberToRemove
		letterCountDict['X'] -= numberToRemove
		
	while letterCountDict['W'] != 0:
		numberToRemove = letterCountDict['W']
		numberOut.extend([2]*numberToRemove)

		letterCountDict['T'] -= numberToRemove
		letterCountDict['O'] -= numberToRemove
		letterCountDict['W'] -= numberToRemove

	#EIgHT
	while letterCountDict['G'] != 0:
		numberToRemove = letterCountDict['G']
		numberOut.extend([8]*numberToRemove)

		letterCountDict['E'] -= numberToRemove
		letterCountDict['I'] -= numberToRemove
		letterCountDict['H'] -= numberToRemove
		letterCountDict['T'] -= numberToRemove
		letterCountDict['G'] -= numberToRemove


	#FOuR
	while letterCountDict['U'] != 0:
		numberToRemove = letterCountDict['U']
		numberOut.extend([4]*numberToRemove)

		letterCountDict['F'] -= numberToRemove
		letterCountDict['O'] -= numberToRemove
		letterCountDict['R'] -= numberToRemove
		letterCountDict['U'] -= numberToRemove


	'''six
			two
			eight
			foUR
			seven
			FIVE
			Nine
			Three
			one'''
	while letterCountDict['S'] != 0:
		numberToRemove = letterCountDict['S']
		doubleNum = numberToRemove*2
		numberOut.extend([7]*numberToRemove)
		
		letterCountDict['E'] -= doubleNum
		letterCountDict['V'] -= numberToRemove
		letterCountDict['N'] -= numberToRemove
		letterCountDict['S'] -= numberToRemove
		

	
		
	#FIvE
	while letterCountDict['V'] != 0:
		numberToRemove = letterCountDict['V']
		numberOut.extend([5]*numberToRemove)

		letterCountDict['F'] -= numberToRemove
		letterCountDict['I'] -= numberToRemove
		letterCountDict['E'] -= numberToRemove
		letterCountDict['V'] -= numberToRemove

	#nIne
	while letterCountDict['I'] != 0:
		numberToRemove = letterCountDict['I']
		doubleNum = numberToRemove*2
		numberOut.extend([9]*numberToRemove)

		letterCountDict['N'] -= doubleNum
		letterCountDict['E'] -= numberToRemove
		letterCountDict['I'] -= numberToRemove
	
	#ThREE
	while letterCountDict['H'] != 0:
		numberToRemove = letterCountDict['H']
		doubleNum = numberToRemove*2
		numberOut.extend([3]*numberToRemove)

		letterCountDict['T'] -= numberToRemove
		letterCountDict['R'] -= numberToRemove
		letterCountDict['E'] -= doubleNum
		letterCountDict['H'] -= numberToRemove
		
	
	#oNE
	while letterCountDict['O'] != 0:
		numberToRemove = letterCountDict['O']
		numberOut.extend([1]*numberToRemove)

		letterCountDict['N'] -= numberToRemove
		letterCountDict['E'] -= numberToRemove
		letterCountDict['O'] -= numberToRemove
		


	finalStringOut = sorted(list((numberOut)))
	finalOut = ''.join(str(e) for e in finalStringOut)
	return finalOut 	#str(sorted(list((numberOut))))
		
jam.run("A-large.in", solve)