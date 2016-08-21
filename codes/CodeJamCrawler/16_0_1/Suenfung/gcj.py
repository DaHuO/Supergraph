import os
import pprint
def main ():
	output = '';
	[inputCount, numList] = readFile()
	for i in range(0,int(inputCount)):
		num = int(numList[i])
		checklist = set()
		find = False
		if num != 0:
			for j in range(1,10**10):
				checklist = checklist.union(set(list(str(num*j))))
				if sorted(checklist) == ['0','1','2','3','4','5','6','7','8','9']:
					p_str = 'Case #{0}: {1}\n'.format((i+1),num*j)
					output += p_str
					print (p_str)
					find = True
					break
		if find == False: 
			p_str = 'Case #{0}: INSOMNIA\n'.format((i+1))
			output += p_str
			print (p_str)
	writeFile(output)

def readFile ():
	with open('A-large.in') as f:
		s = f.read()
	s = s.split('\n')
	inputCount = s.pop(0);
	s.pop(-1)
	return [inputCount,s]

def writeFile (str):
	with open('A-large.out', 'w') as f:
		f.write(str)

if __name__ == '__main__':
	main()