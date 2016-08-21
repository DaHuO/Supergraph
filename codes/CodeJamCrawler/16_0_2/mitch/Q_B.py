#!/usr/bin/env python3.5

T = int(input())

def solve(s):
	result = 0
	
	last = s[0]
	for i in range(1, len(s)):
		if last == s[i]:
			pass
		else:
			result += 1
			last = s[i]
			
	if last == '-':
		result += 1
	
	return result

for t in range(1, T+1):
	print("Case #{}: {}".format(t, solve(input())))

