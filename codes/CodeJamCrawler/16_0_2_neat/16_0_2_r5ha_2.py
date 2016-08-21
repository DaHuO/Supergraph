#!/usr/bin/python3

from itertools import count

def main():
	f = open('../test_files/input', 'r')
	w = open('../test_files/output', 'w')
	t = int(f.readline().strip())
	for i in range(1, t+1):
		w.write('Case #%d: ' % i)
		s = f.readline().strip()
		w.write(result(s) + '\n')
	w.close()
	
def result(s):
	s_ = list(s)
	n = result_(s_)
	if s_[0] == '-':
		n = n + 1
	return str(n)
	
def result_(s):
	for n in count():
		assert(n < len(s))
		for i in range(len(s) + 1):
			if i == len(s):
				return n
			if s[i] != s[0]:
				break
		for j in range(i):
			if s[j] == '-':
				s[j] = '+'
			else:
				s[j] = '-'

if __name__ == '__main__':
	main()