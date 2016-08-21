import string
T = int(raw_input())
for i in range(1, T + 1):
	print "Case #%d:" % i,
	S = raw_input()
	ansleft = ""
	ansright = ""
	while S:
		for j in string.uppercase[::-1]:
			now = S.rfind(j)
			if now != -1:
				ansleft += j
				ansright = S[now + 1:] + ansright
				S = S[:now]
				break
	print ansleft + ansright