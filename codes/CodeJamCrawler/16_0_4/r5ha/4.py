#!/usr/bin/python3

from math import ceil

def main():
	f = open('../test_files/input', 'r')
	w = open('../test_files/output', 'w')
	t = int(f.readline())
	for i in range(1, t+1):
		w.write('Case #%d: ' % i)
		k, c, s = [int(x) for x in f.readline().strip().split()]
		w.write(result(k, c, s) + '\n')
	w.close()
	
def result(k, c, s):
	if ceil(k / c) > s:
		return 'IMPOSSIBLE'
	return ' '.join([str(x + 1) for x in result_(k, c, s)])
	
def result_(k, c, s):
	for i in range(0, k, c):
		if i + c <= k:
			path = range(i, i + c)
		else:
			path = list(range(i, k)) + ([0] * (i + c - k))
		yield path_to_num(k, c, path)
		
def path_to_num(k, c, path):
	num = 0
	for i in range(c):
		num = num * k + path[i]
	return num

if __name__ == '__main__':
	main()