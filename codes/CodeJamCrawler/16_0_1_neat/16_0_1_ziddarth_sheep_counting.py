import os
from collections import OrderedDict


def sheep():
	max_j = 0
	result_dict = {0: 'INSOMNIA'}
	for i in range(1, 1000001):
		s = OrderedDict()
		for j in range(1, 73):
			for n in str(i * j):
				s[str(n)] = 1
			if len(s) == 10:
				max_j = max(max_j, j)
				result_dict[i] = i * j
				#             print s
				#             print i, '#', 'j=',j, 'answer=', (i * j), s.keys()
				break
		# no break
		else:
			print 'FAILED', i
	print 'DONE,max_j=', max_j
	return result_dict


def main():
	result = sheep()

	# 'A-small-attempt0.in'
	filename = raw_input('Enter input filename:').strip()
	while os.path.exists(filename):
		output = filename.replace('.in', '.out')
		with open(filename, 'r') as f, open(output, 'w') as out:
			t = int(f.readline())
			i = 1
			while t:
				n = int(f.readline())
				out.write('Case #{}: {}\n'.format(i, result[n]))
				t -= 1
				i += 1
		print 'Wrote output -> ' + output
		filename = raw_input('Enter input filename:').strip()

if __name__ == '__main__':
	main()
