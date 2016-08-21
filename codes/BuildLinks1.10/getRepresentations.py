#!/usr/bin/env python
# -*- coding: utf-8 -*-


def getReps(code, majortoken, threshold):
	coderep = {}
	codeminorrep = {}
	for line in code:
		represult = []
		minorrep = []
		major = []
		n = int(len(code[line]) * (1 -threshold))
		for token in code[line]:
			if token in majortoken:
				major.append(token)
			else:
				minorrep.append(token)
		if len(minorrep) >= n:
			represult = minorrep[:n]
		else:
			represult = list(minorrep)
			represult.extend(major[len(minorrep):n])
		coderep[line] = list(represult)
		codeminorrep[line] = list(minorrep)
	return coderep, codeminorrep




if __name__ == '__main__':
	getReps()