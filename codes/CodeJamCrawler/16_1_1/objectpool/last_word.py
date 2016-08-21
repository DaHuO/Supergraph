

n = int(str(input()))

for i in range(n):
	s = input()
	def last_word(s):
		if len(s) == 1:
			return s
		first_letter = s[0]
		word = s[0]
		for index in range(1,len(s)):
			if s[index] >= word[0]:
				word = s[index] + word
			else:
				word += s[index]
		return word
	print('Case #'+str(i+1)+': ' + last_word(s))