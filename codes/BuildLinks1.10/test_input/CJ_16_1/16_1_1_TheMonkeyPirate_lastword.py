n = int(input())
case = 0

while (n):
	n -= 1
	case += 1

	word = input()
	final = ''

	for i in range(len(word)):
		char = word[i]
		if len(final) == 0:
			final += char
			continue
		if ord(char[0]) >= ord(final[0]):
			final = char + final
		else:
			final += char

	print('Case #', case, ': ', final, sep='')
