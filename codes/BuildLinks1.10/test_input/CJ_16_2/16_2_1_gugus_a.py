#!/usr/bin/python

import sys

def remove(line, c):
	return line[:line.find(c)]+line[line.find(c)+1:]

def solve(line):
	ans = ""
	while (line.find('Z')!=-1):
		line = remove(line, 'Z')
		line = remove(line, 'E')
		line = remove(line, 'R')
		line = remove(line, 'O')
		ans += "0"
	while (line.find('W')!=-1):
		line = remove(line, 'T')
		line = remove(line, 'W')
		line = remove(line, 'O')
		ans += "2"
	while (line.find('G')!=-1):
		line = remove(line, 'E')
		line = remove(line, 'I')
		line = remove(line, 'G')
		line = remove(line, 'H')
		line = remove(line, 'T')
		ans += "8"
	while (line.find('H')!=-1):
		line = remove(line, 'T')
		line = remove(line, 'H')
		line = remove(line, 'R')
		line = remove(line, 'E')
		line = remove(line, 'E')
		ans += "3"
	while (line.find('X')!=-1):
		line = remove(line, 'S')
		line = remove(line, 'I')
		line = remove(line, 'X')
		ans += "6"

	while (line.find('S')!=-1):
		line = remove(line, 'S')
		line = remove(line, 'E')
		line = remove(line, 'V')
		line = remove(line, 'E')
		line = remove(line, 'N')
		ans += "7"
	while (line.find('R')!=-1):
		line = remove(line, 'F')
		line = remove(line, 'O')
		line = remove(line, 'U')
		line = remove(line, 'R')
		ans += "4"

	while (line.find('F')!=-1):
		line = remove(line, 'F')
		line = remove(line, 'I')
		line = remove(line, 'V')
		line = remove(line, 'E')
		ans += "5"
	while (line.find('O')!=-1):
		line = remove(line, 'O')
		line = remove(line, 'N')
		line = remove(line, 'E')
		ans += "1"
	while (line.find('N')!=-1):
		line = remove(line, 'N')
		line = remove(line, 'I')
		line = remove(line, 'N')
		line = remove(line, 'E')
		ans += "9"
	return ''.join(sorted(list(ans)))
		
def main():
	with open(sys.argv[1], 'r') as f:
		n = int(f.readline())
		lines = [f.readline() for i in xrange(n)]
	for i in xrange(n):
		
		print('Case #%d: %s' % (i+1, solve(lines[i])))

if __name__ == '__main__':
	main()
