#!/usr/bin/env python
# -*- coding: utf-8 -*-


def getReps(code, majortoken, threshold, GTP):
	coderep = {}
	codeminorrep = {}
	# for line in code:
	# 	represult = []
	# 	minorrep = []
	# 	major = []
	# 	n = int(len(code[line]) * (1 -threshold))
	# 	for token in code[line]:
	# 		if token in majortoken:
	# 			major.append(token)
	# 		else:
	# 			minorrep.append(token)
	# 	if len(minorrep) >= n:
	# 		represult = minorrep[:n]
	# 	else:
	# 		represult = list(minorrep)
	# 		represult.extend(major[len(minorrep):n])
	# 	coderep[line] = list(represult)
	# 	codeminorrep[line] = list(minorrep)
	for line in code:
		represult = []
		minorrep = []
		major = []
		minor = []
		coderep[line] = []
		nt = min(int(len(code[line]) * (1 - threshold)) + 1, len(code[line]))
		n = len(code[line])
		for pos, token in enumerate(code[line]):
			if token in majortoken:
				major.append((token, pos))
				# major.append((token, pos, max((pos - n - int(threshold * n)), 0), n - pos, max(int(n * threshold) - pos, 0)))
				#token, maxleft, minleft, maxright, minright
			else:
				minor.append((token, pos))
				# minorrep.append((token, pos, max((pos - n - int(threshold * n)), 0), n - pos, max(int(n * threshold) - pos, 0)))
				minorrep.append(token)
		if len(minor) >= nt:
			represult = minor[:nt]
		else:
			represult = list(minor)
			represult.extend(major[len(minor):n])
		for token, pos in represult:
			coderep[line].append((token, pos, max((pos - n + int(threshold * n)), 0), n - pos, max(int(n * threshold) - pos, 0)))
		# coderep[line] = list(represult)
		codeminorrep[line] = list(minorrep)


	return coderep, codeminorrep




if __name__ == '__main__':
	getReps()