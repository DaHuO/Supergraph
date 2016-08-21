import sys
import os

def addLetter(word,letter):
	if(word[:1]==letter):
		return letter+word
	if(min(word[:1],letter)!=letter):
		return letter+word
	else:
		return word+letter

def processSequence(word):
	curWord = word[:1]
	for x in ''.join(word[1:]):
		curWord = addLetter(curWord,x)
	return curWord

def main():
	f = open("A-large.in",'r')
	fTwo = open("lastword.out",'w')
	t = int(f.readline())
	for x in range(t):
		fTwo.write("Case #"+str(x+1)+": "+processSequence(f.readline()))
	f.close()
	fTwo.close()
	final = open("lastword.out",'r')
	print(final.read())
	final.close()
if __name__ == "__main__":
	main()
