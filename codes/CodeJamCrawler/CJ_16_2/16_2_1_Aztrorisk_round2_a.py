

from Library import *
import math

def solve(n):
	strBuilt = ""
	counts = [0 for x in range(10)]
	mapx = {}
	mapx['Z'] = 0
	mapx['W'] = 0
	mapx['U'] = 0
	mapx['X'] = 0
	mapx['G'] = 0
	mapx['H'] = 0
	mapx['F'] = 0
	mapx['S'] = 0
	mapx['O'] = 0
	mapx['I'] = 0
	for i in range(len(n)):
		if mapx.has_key(n[i]):
			mapx[n[i]] += 1
		else:
			mapx[n[i]] = 1

	counts[0] = mapx['Z']
	if counts[0] > 0:
		mapx['Z'] -= counts[0]
		mapx['E'] -= counts[0]
		mapx['R'] -= counts[0]
		mapx['O'] -= counts[0]

	counts[2] = mapx['W']
	if counts[2] > 0:
		mapx['T'] -= counts[2]
		mapx['W'] -= counts[2]
		mapx['O'] -= counts[2]

	
	counts[4] = mapx['U']
	if counts[4] > 0:
		mapx['F'] -= counts[4]
		mapx['O'] -= counts[4]
		mapx['U'] -= counts[4]
		mapx['R'] -= counts[4]

	counts[6] = mapx['X']
	if counts[6] > 0:
		mapx['S'] -= counts[6]
		mapx['I'] -= counts[6]
		mapx['X'] -= counts[6]

	counts[8] = mapx['G']
	if counts[8] > 0:
		mapx['E'] -= counts[8]
		mapx['I'] -= counts[8]
		mapx['G'] -= counts[8]
		mapx['H'] -= counts[8]
		mapx['T'] -= counts[8]

	counts[3] = mapx['H']
	if counts[3] > 0:
		mapx['T'] -= counts[3]
		mapx['H'] -= counts[3]
		mapx['R'] -= counts[3]
		mapx['E'] -= counts[3]
		mapx['E'] -= counts[3]

	counts[5] = mapx['F']
	if counts[5] > 0:
		mapx['F'] -= counts[5]
		mapx['I'] -= counts[5]
		mapx['V'] -= counts[5]
		mapx['E'] -= counts[5]

	counts[7] = mapx['S']
	if counts[7] > 0:
		mapx['S'] -= counts[7]
		mapx['E'] -= counts[7]
		mapx['V'] -= counts[7]
		mapx['E'] -= counts[7]
		mapx['N'] -= counts[7]

	counts[1] = mapx['O']
	if counts[1] > 0:
		mapx['O'] -= counts[1]
		mapx['N'] -= counts[1]
		mapx['E'] -= counts[1]

	counts[9] = mapx['I']
	if counts[9] > 0:
		mapx['N'] -= counts[9]
		mapx['I'] -= counts[9]
		mapx['N'] -= counts[9]
		mapx['E'] -= counts[9]

	for i in range(10):
		for j in range(counts[i]):
			strBuilt += str(i)

	return strBuilt



lines = getLines("A-large.in")
out = []

for i in range(int(lines[0])):
	value = list(lines[i + 1].replace("\n", ""))
	res = solve(value)
	out.append("Case #%d: %s"%(i + 1, res))

writeOutLines("out.txt", out)