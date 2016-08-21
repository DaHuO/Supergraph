

output = ""

with open("b.in", "a+") as f:
	data = f.read().split("\n")


def inverse(ch):
	return "+" if ch == '-' else '-'


for l in range(0,int(data[0])):
	st = [x for x in data[l+1].strip()]


	lim = 0

	while st.count("+") != len(st):
		fst = st[0]
		idx = "".join(st).find(inverse(fst))
		idx = len(st) if idx == -1 else idx
		for x in range(0,idx):
			st[x] = inverse(fst)
		lim+=1

	output+= "Case #%s: %s\n" % (str(l+1), str(lim))



with open("b.out","w+") as f:
	f.write(output)	



