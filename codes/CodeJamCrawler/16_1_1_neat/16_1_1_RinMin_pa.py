from sys import *

def max_el(s, bot, top):
	big = s[bot]
	big_i = bot
	for i in range(bot, top):
		if s[i] >= big:
			big = s[i]
			big_i = i
	return big_i

def spell_word(s):
	places = []
	for c in s:
		places.append('F')
	i = len(s)-1
	while i > 0:
		j = max_el(s, 0, i)
		places[j] = 'F'
		for p in range(j+1, i):
			places[p] = 'B'
		i = j
	
	res = ""
	for i in range(0, len(s)-1):
		if places[i] == 'F':
			res = s[i] + res
		else:
			res = res + s[i]
	return res

fin = open(argv[1] + ".in", 'r') 
fout = open(argv[1] + ".out", 'w')

ncases = int(fin.readline())
for c in range(0, ncases):
	fout.write("Case #" + str(c+1) + ": " + spell_word(fin.readline()) + "\n")

fin.close()
fout.close()


	
