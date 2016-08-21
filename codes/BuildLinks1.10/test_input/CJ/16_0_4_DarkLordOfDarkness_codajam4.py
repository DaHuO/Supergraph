#!/usr/bin/python

import math

txt = open("D-small-attempt1 (1).in", "r")

out = open("a.txt", "w")
dic = {}
case = 0

for k in range(int(txt.readline().strip())):
	for i in txt:
		case = case + 1
		metr = 1
		i = i.split(' ')
		count = int(i[1])
		out.write("Case #"+  str(case) + ":")
		if int(i[1]) == 1 or int(i[0]) == int(i[2]):
			if int(i[0]) > int(i[2]):
				out.write(" IMPOSSIBLE\n")
			else:
				for j in range(int(i[0])) :
					out.write(" " + str(j + 1))
				out.write('\n')
		elif math.log(int(i[0]), int(i[1])) > int(i[2]):
			out.write(" IMPOSSIBLE\n")
		else:
			j = 0 
			while j < int(i[0]):
				while count > 0 and j < int(i[0]):
					count = count - 1
					metr = metr + pow(int(i[0]),count) * j
					j = j + 1
				out.write(' ' + str(metr))
				metr = 1
				count = int(i[1])
				j = j + 1
			out.write('\n')
		"	out.write(' ' + str(metr) + '   count  '+ str(count) +  '\n')"