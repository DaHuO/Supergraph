input = open('A-large.in', 'r')
output = open('output.txt', 'w')
output.seek(0)
output.truncate()
T = int(input.readline())
case = 0

for i, line in enumerate(input):
	if case < T:
		last_word = ''
		first = ''
		for ch in line:
			if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
				if ch >= first:
					last_word = ch + last_word
					first = ch
				else:
					last_word = last_word + ch
		case = case + 1
		output.write("Case #%d: %s\n" % (case, last_word))
output.close()
input.close()