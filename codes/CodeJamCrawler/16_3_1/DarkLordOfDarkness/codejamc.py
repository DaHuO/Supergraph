#!/usr/bin/python

import math

txt = open("A-small-attempt2.in", "r")

out = open("a.txt", "w")

def getKey(item):
	return item[0]

dic = {}
case = 0

for k in range(int(txt.readline().strip())):
	tpt = []
	txt.readline()
	i = txt.readline()
	case = case + 1
	i = i.strip().split()
	out.write("Case #"+  str(case) + ":")
	for j in range(len(i)):
		tpt.append([i[j], chr(ord('A') + j)])
	tpt = sorted(tpt, key = getKey, reverse = True)
	b = sum(map(int,i))
	
	if b % 2 == 1 :
		save = []
		tpt[0][0] = int(tpt[0][0]) - 1
		save.append(tpt[0][1])
		out.write(' ' + ''.join(save))
		tpt = sorted(tpt, key = getKey, reverse = True)

	while int(tpt[0][0]) != 0 :
		save = []
		tpt[0][0] = int(tpt[0][0]) - 1
		save.append(tpt[0][1])
		tpt = sorted(tpt, key = getKey, reverse = True)
		if int(tpt[0][0]) != 0 :
			tpt[0][0] = int(tpt[0][0]) - 1
			save.append(tpt[0][1])
			tpt = sorted(tpt, key = getKey, reverse = True)
		out.write(' ' + ''.join(save))
	out.write('\n')