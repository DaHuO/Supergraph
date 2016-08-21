import string
import math

txt = open("A-large.in", "r")

out = open("a.txt", "w")

dict = {}
list = [0] * 11
case = 0

for i in string.uppercase:
	dict[i] = 0

for k in range(int(txt.readline().strip())):
	case = 0
	for i in txt:
		dict = {}
		list = [0] * 11

		for aoua in string.uppercase:
			dict[aoua] = 0
		case = case + 1
		metr = 0
		i = i.strip()
		out.write("Case #"+  str(case) + ": ")
		for char in i:
			if char == 'Z' :
				list[0] += 1
				dict['Z'] -=1
				dict['E'] -=1
				dict['R'] -=1
				dict['O'] -=1
			elif char == 'W' :
				list[2] += 1
				dict['T'] -=1
				dict['W'] -=1
				dict['O'] -=1
			elif char == 'U' :
				list[4] += 1
				dict['F'] -=1
				dict['O'] -=1
				dict['U'] -=1
				dict['R'] -=1
			elif char == 'X':
				list[6] += 1
				dict['S'] -=1
				dict['I'] -=1
				dict['X'] -=1
			elif char == 'G':
				list[8] += 1
				dict['E'] -=1
				dict['I'] -=1
				dict['G'] -=1
				dict['H'] -=1
				dict['T'] -=1				
			else :
				dict[char] += 1
		
		if dict['S'] > 0 :
			list[7] = dict ['S']
			for aaa in range(list[7]):
				dict['S'] -=1
				dict['E'] -=1
				dict['V'] -=1
				dict['E'] -=1
				dict['N'] -=1
		if dict['F'] > 0 :
			list[5] = dict ['F']
			for aaa in range(list[5]):
				dict['F'] -=1
				dict['I'] -=1
				dict['V'] -=1
				dict['E'] -=1
				
		if dict['H'] > 0 :
			list[3] = dict ['H']
			for aaa in range(list[3]):
				dict['T'] -=1
				dict['H'] -=1
				dict['R'] -=1
				dict['E'] -=1
				dict['E'] -=1		
				
		if dict['O'] > 0 :
			list[1] = dict ['O']
			for aaa in range(list[1]):
				dict['O'] -=1
				dict['N'] -=1
				dict['E'] -=1
		
		if dict['I'] > 0 :
			list[9] = dict ['I']
			for aaa in range(list[9]):
				dict['N'] -=1
				dict['I'] -=1
				dict['N'] -=1
				dict['E'] -=1

		for aba in range(10):
			for aza in range(list[aba]):
				out.write(str(aba))
				
		out.write('\n')


				