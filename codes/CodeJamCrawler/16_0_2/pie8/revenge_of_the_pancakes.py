#!/usr/bin/env python

def flip(p): return "+" if p == "-" else "-"

def maneuver(p, p_nb): return map(flip, p[:p_nb]) + p[p_nb:]

def solve(pancakes):
	if pancakes == "-": return 1
	pancakes = list(pancakes)
	maneuvers = 0

	while pancakes.count("+") != len(pancakes):
		state = pancakes[0]
		i = 1

		while i < len(pancakes):
			if state == "-":
				if pancakes[i] == "+":
					pancakes = maneuver(pancakes, i)
					maneuvers += 1
					break
				elif i == len(pancakes)-1:
					pancakes = maneuver(pancakes, len(pancakes))
					maneuvers += 1
					break
			elif state == "+" and pancakes[i] == "-":
				state = "-"
				if i == len(pancakes)-1:
					pancakes = maneuver(pancakes, len(pancakes))
					maneuvers += 1
					break
			i += 1

	return maneuvers

def main():
	testcase_nb = long(raw_input().strip())
	i = 1

	with open('revenge_of_the_pancakes.out', 'w') as outfile:
		while i <= testcase_nb:
			pancakes = raw_input().strip()
			maneuvers = solve(pancakes)
			outfile.write("Case #%d: %s\n" % (i, maneuvers))
			i += 1

if __name__ == '__main__':
	main()
