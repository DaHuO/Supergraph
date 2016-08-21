file = open('last_word.txt', 'r')
out = open('last_word_out.txt', 'w')

t = int(file.readline())
for i in xrange(0, t):
	s = file.readline()
	s = s[:len(s)-1]

	ans = s[0]
	for j in xrange(1, len(s)):
		if s[j] >= ans[0]:
			ans = s[j] + ans
		else:
			ans = ans + s[j]
	out.write("Case #" + str(i +1) + ": " + ans + "\n")

