import os
import pprint
def main ():
	output = '';
	[inputCount, pancakeList] = readFile()
	for i in range(0,int(inputCount)):#no need to match last item
		pancake = pancakeList[i]
		print('pancake: %s'%pancake)
		count = 0
		if pancake[-1] == '-':
			count = 1
		for j in range(0,len(pancake)-1):
			print('pancake[j]: %s'%pancake[j])
			print('pancake[j+1]: %s'%pancake[j+1])
			if pancake[j] != pancake[j+1]:
				count+=1
		p_str = 'Case #{0}: {1}\n'.format((i+1),count)
		output += p_str
		print ('		%s'%p_str[0:-1])
	writeFile(output)

def readFile ():
	with open('B-large.in') as f:
		s = f.read()
	# s = '9\n-\n+\n-+\n+-\n+++\n--=-\n--+--+\n-+-+-+\n+-+-+-\n'
	s = s.split('\n')
	inputCount = s.pop(0);
	s.pop(-1)
	return [inputCount,s]

def writeFile (str):
	with open('B-large.out', 'w') as f:
		f.write(str)

if __name__ == '__main__':
	main()