#!/bin/env python3

import sys
import os


def doChallenge(_input_filename):
	try:
		with open(_input_filename, 'r') as f:
			lines = f.read().split('\n')
	except FileNotFoundError:
		print("Input file '" + _input_filename + "' not found !")
		sys.exit()
	except PermissionError:
		print("Input file '" + _input_filename + "' could not be read !")
		sys.exit()
	except Exception:
		print("Unknown shit has happened")
		sys.exit()

	del lines[0] # First line is useless
	for i in range(len(list(filter(None, lines)))):
		init = lines[i]
		seen = list(set(init))
		for j in range(2,100000):
			_ = int(init)*j
			seen = sorted(list(set(seen + list(set(str(_))))))
			if seen == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
				print("Case #" + str(i+1) + ": " + str(_))
				break
		if j == 99999:
			print("Case #" + str(i+1) + ": INSOMNIA")



if __name__ == '__main__':
	try:
		sys.argv[1]
	except IndexError:
		print("Usage : " + sys.argv[0] + " filename")
	else:
		doChallenge(sys.argv[1])
