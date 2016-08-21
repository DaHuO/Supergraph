
def algo(line):
	a = line.split(' ')
	K = int(a[0])
	C = int(a[1])
	S = int(a[2])
	#print (K, C, S)
	if K == S:
		return [str(a) for a in range(1,K+1)]
	elif K > S*C:
		return ['IMPOSSIBLE']
	else:
		val = 1
		c = []
		for a in range(1, K//C + 1):
			for b in range(0, b):
				val *= C
				val += C
			c.append(str(val))
		return c
		


if __name__ == '__main__':
	
	fout = open('D-small.out', 'w')

	with open('D-small-attempt0.in','r') as fin:
		number_of_cases = fin.readline()

		case = 1
		for line in fin.readlines():
			#print(line)
			ans = algo(line)
			fout.write("Case #{0}: {1}\n".format(str(case), ' '.join(ans)))
			case += 1
