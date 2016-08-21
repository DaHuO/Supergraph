from collections import OrderedDict
T = int (input())
for i in range (0, T):
        N = int (input())
	number = i + 1
	sen = {}
	c = raw_input()
	j = 0
	for P in c.split():
		sen [chr(ord('A') + j)] = int(P)
		j = j + 1
	lis = list (sorted(sen.keys(), key = sen.get, reverse=True))
	s = ""
	ch = lis[0]
	while (sen [ch] != 0):
		s += str(lis[0])
		sen [ch] -= 1
		lis = list (sorted(sen, key = sen.get, reverse=True))
		ch = lis [0]
	s = s[::-1]
	s = " ".join(s[k:k+2] for k in range (0, len(s), 2))
	s = s [::-1]
	ans = "Case #"
	ans += str (number)
	ans += ": "
	ans += s
	ans += " "
        print(ans)
