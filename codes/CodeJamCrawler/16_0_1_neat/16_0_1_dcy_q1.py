# -*- coding: utf-8 -*-

import pdb

def solve(num):
	if num == 0:
		return "INSOMNIA"
	num_set = set()
	i = 1
	while True:
		num_set = num_set | set([int(x) for x in str(i * num)])
		if num_set == set(range(10)):
			return i * num
		else:
			i += 1

def main():
	results = []

	with open('A-large.in.txt', 'r') as f:
		case_total = int(f.readline().strip())
		for i in range(case_total):
			line = f.readline().strip()
			results.append(solve(int(line)))

	with open('out', 'w') as f:
		for i in range(len(results)):
			f.write('Case #{0}: {1}\n'.format(i+1, results[i]))	

if __name__ == '__main__':
	main()



