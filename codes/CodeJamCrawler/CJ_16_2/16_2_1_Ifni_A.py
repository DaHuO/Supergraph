import math
import numpy as np

def remove(S, nb, arr):
	for s in list(S):
		arr[ord(s)-65]=arr[ord(s)-65]-nb;


inp=open('A-large.in', 'r')
out=open("output-A-large", 'w')

T=int(inp.readline())
for index in range(T):
	S=inp.readline()[:-1]
	print S
	letters=np.zeros((26,1))
	numbers=np.zeros((10,1))
	for char in S:
		letters[ord(char)-65]=letters[ord(char)-65]+1

	numbers[0]=letters[ord('Z')-65];
	for s in "ZERO":
		letters[ord(s)-65]=letters[ord(s)-65]-numbers[0];

	numbers[2]=letters[ord('W')-65];
	for s in "TWO":
		letters[ord(s)-65]=letters[ord(s)-65]-numbers[2];

	numbers[6]=letters[ord('X')-65];
	for s in "SIX":
		letters[ord(s)-65]=letters[ord(s)-65]-numbers[6];

	numbers[8]=letters[ord('G')-65];
	for s in "EIGHT":
		letters[ord(s)-65]=letters[ord(s)-65]-numbers[8];


	numbers[3]=letters[ord('H')-65];
	for s in "THREE":
		letters[ord(s)-65]=letters[ord(s)-65]-numbers[3];

	numbers[4]=letters[ord('R')-65];
	for s in "FOUR":
		letters[ord(s)-65]=letters[ord(s)-65]-numbers[4];

	numbers[5]=letters[ord('F')-65];
	for s in "FIVE":
		letters[ord(s)-65]=letters[ord(s)-65]-numbers[5];

	numbers[9]=letters[ord('I')-65];
	for s in "NINE":
		letters[ord(s)-65]=letters[ord(s)-65]-numbers[9];

	numbers[7]=letters[ord('S')-65];
	for s in "SEVEN":
		letters[ord(s)-65]=letters[ord(s)-65]-numbers[7];

	numbers[1]=letters[ord('O')-65];
	for s in "ONE":
		letters[ord(s)-65]=letters[ord(s)-65]-numbers[1];						

	answer=""
	for i in range(10):
		for j in range(numbers[i]):
			answer=answer+str(int(i))

	out.write('Case #{}: {}\n'.format(index+1, answer))




inp.close()
out.close()