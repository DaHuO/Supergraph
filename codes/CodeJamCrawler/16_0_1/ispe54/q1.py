#!coding=utf-8
import sys

def main():
	t = int(raw_input())
	for i in range(1, t+1):
		n = int(raw_input())
		if n == 0:
			print 'Case #%d:' % i, 'INSOMNIA'
			continue
		digits = [0] * 10
		start = 0
		while 1:
			start = start+n
			ds = str(start)
			for c in ds:
				idx = ord(c) - ord('0')
				digits[idx] = 1
			if sum(digits) == 10:
				print 'Case #%d:' % i, start
				break
		continue
	return

if __name__ == '__main__':
	main()