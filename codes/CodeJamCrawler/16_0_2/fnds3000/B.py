#! /usr/bin/python

def solve(s):
	solution = 0
	for c in s[::-1]:
		if (c=='-' and solution%2==0) or (c=='+' and solution%2==1):
			solution += 1
	return solution

def main():
	t = int(raw_input())
	for i in range(1, t+1):
		s = raw_input()
		print("Case #%d: %d" % (i, solve(s)))

if __name__=="__main__":
	main()