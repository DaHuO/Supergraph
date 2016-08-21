import sys
import os

#simplifies patterns
def simplify(pattern):
	newPattern = [list(pattern)[0]]
	for x in list(pattern):
		if (x != newPattern[-1]):
			newPattern.append(x)
	return ''.join(newPattern).rstrip()
#flips pancake stack and simplifies
def flip(pattern):
	newPattern = []
	for x in list(pattern):
		if(x=='-'):
			x='+'
		else:
			if(x=='+'):
				x='-'
		newPattern.insert(0,x)
	return simplify(''.join(newPattern)).rstrip()
#run one pattern
def pancake(pattern):
	flips = 0
	pattern = simplify(pattern)
	print('[*] Pattern is '+pattern+'.')
	if(pattern=='+'):
		print('[+] Short circuit with +')
		return 0
	if(pattern=='-'):
		print('[+] Short circuit with -')
		return 1
	if(pattern=='-+'):
		return 1
	if(pattern=='+-'):
		return 2
	print('[*] At least 3 long')
	while(len(list(pattern))>3):
		flips = flips+1
		pattern = simplify(flip(pattern[0:3])+pattern[3:])
	if(pattern=='+-+'):
		return flips+2
	if(pattern=='-+-'):
		return flips+3
	return flips+2
#main
def main():
	f = open('B-large.in','r')
	fTwo = open('B-pancake.out','w')
	t = int(f.readline())
	print('[+] Beginning iterations')
	for x in range(t):
		fTwo.write('Case #'+str(x+1)+': '+str(pancake(f.readline()))+'\n') 
		print('[+] Iteration '+str(x+1)+' complete')
	f.close()
	fTwo.close()
	print(open('pancake.out','r').read())
if __name__ == '__main__':
	main()
