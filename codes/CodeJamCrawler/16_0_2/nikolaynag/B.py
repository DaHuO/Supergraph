#!/usr/bin/env python
import sys

lines = [l.strip() for l in sys.stdin.readlines()]
T = int(lines[0])
assert(T == len(lines)-1)

def inverted_pancakes(s):
	return s.replace("+", "1").replace("-", "+").replace("1","-")	

#"++-.++++" -> "++.-----" -> "+++++++"
#"++.-++++" -> "+++.----" -> "+++++++"

def min_pancake_maneuvers(s):
	n = 0
	while s:
		ix = s.find("-")
		if ix < 0:
			break
		s = inverted_pancakes(s[ix:])
		n += 1
	return n

for i in range(1, T+1):
	sys.stdout.write("Case #{}: {}\n".format(i, min_pancake_maneuvers(lines[i][::-1])))
