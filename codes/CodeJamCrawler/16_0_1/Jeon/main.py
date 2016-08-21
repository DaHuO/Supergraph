#! /usr/bin/env python3

import sys

def calc(n):
	s = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
	num = 0
	if n:
		while len(s):
			num = num + n
			s_ = set([int(x) for x in str(num)])
			s = s - s_
#			print('s_: ', s_)
#			print('s : ', s)
	return num


def main(file_name):
	with open(file_name, 'rU') as file_in:
		t = int(file_in.readline())
		for i in range(t):
			n = int(file_in.readline())
#			print('n : ', n)
			num = calc(n)
			print('Case #{0}: {1}'.format(i+1, num if num else 'INSOMNIA'))
				

if __name__ == "__main__":
	f = sys.argv[1]
	main(f)
