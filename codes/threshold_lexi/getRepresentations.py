#!/usr/bin/env python
# -*- coding: utf-8 -*-


def getReps(code, majortoken, threshold):
	coderep = {}
	codeminorrep = {}
	countline = 0
	countyes = 0
	for line in code:
		countline += 1
		represult = []
		minorrep = []
		major = []
		n = int(len(code[line]) * (1 -threshold))
		# print len(code[line]), n
		for token in code[line]:
			if token not in majortoken:
				minorrep.append(token)
			else:
				major.append(token)
		if len(minorrep) >= n:
			countyes += 1
			represult = minorrep[:n]
		else:
			# print 'herhe'
			represult = list(minorrep)
			represult.extend(major[len(minorrep):n])
		coderep[line] = represult
		codeminorrep[line] = minorrep
	# return coderep, codeminorrep
	return countline, countyes




if __name__ == '__main__':
	getReps()