#!/usr/bin/python


txt = open("A-large.in", "r")
out = open("a.txt", "w")
dic = {}
case = 0

for k in range(int(txt.readline().strip())):
	for i in txt:
		case = case + 1
		i.strip()
		i = int(i)
		ua = i
		if ua == 0 :
			out.write("Case #"+  str(case) + ": INSOMNIA\n")
		else:
			while len(dic) < 10:
				st = str(ua)
				for j in range(len(st)):
					dic[st[j]] = 1
				ua = ua + i
			ua = ua -i
			out.write("Case #"+  str(case) + ": " + str(ua) + "\n")
			dic.clear()
