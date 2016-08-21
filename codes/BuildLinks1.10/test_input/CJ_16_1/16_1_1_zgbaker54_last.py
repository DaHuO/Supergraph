file = open('A-large (1).txt')

lines = file.readlines()

output = open('alphasort.txt','w')

testcases = int(lines[0])

def change(x):
	x = x.lower()
	if x == 'st':
		return 0
	if x == 'a':
		return 1
	if x == 'b':
		return 2
	if x == 'c':
		return 3
	if x == 'd':
		return 4
	if x == 'e':
		return 5
	if x == 'f':
		return 6
	if x == 'g':
		return 7
	if x == 'h':
		return 8
	if x == 'i':
		return 9
	if x == 'j':
		return 10
	if x == 'k':
		return 11
	if x == 'l':
		return 12
	if x == 'm':
		return 13
	if x == 'n':
		return 14
	if x == 'o':
		return 15
	if x == 'p':
		return 16
	if x == 'q':
		return 17
	if x == 'r':
		return 18
	if x == 's':
		return 19
	if x == 't':
		return 20
	if x == 'u':
		return 21
	if x == 'v':
		return 22
	if x == 'w':
		return 23
	if x == 'x':
		return 24
	if x == 'y':
		return 25
	if x == 'z':
		return 26


i = 1

while i <= testcases:
	word = lines[i]
	#print('word is ' + word)
	new = ''
	ctr = 0
	while ctr < len(word):
		char = word[ctr]
		newnum = change(word[ctr])
		#print('newnum is ' + str(newnum))
		if len(new) != 0:
			old = change(new[0])
			#print('old is ' + str(old))
		if len(new) == 0:
			#print 1
			new = new + char
		elif newnum > old:
			#print 2
			new = char + new
		elif newnum < old:
			#print 3
			new  = new + char
		else:
			#print 4
			v = 1
			rem = 'st'
			while v < len(new):
				if new[v] != char:
					rem = new[v]
					break
				v = v + 1
			if v == 0:
				new = new + char
			else:
				if newnum > change(rem):
					new = char + new
				elif newnum < change(rem):
					new  = new + char
		ctr = ctr + 1
	outline = 'Case #' + str(i) + ': ' + new
	output.write(outline)
	i = i + 1

file.close()
output.close()