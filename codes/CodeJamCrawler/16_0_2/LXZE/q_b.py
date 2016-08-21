f = open("B-large.in","r")
w = open("output_lb.txt","w")
num = f.readline()

for it in range(0,int(num)):
	pancakes = f.readline().rstrip('\n')
	res = 0
	state = ''
	txt = ''
	for ch in pancakes:
		if state != ch:
			txt+=ch
		state = ch

	if txt[0] == '-':
		res += 1
		txt = txt[1:]
	for ch in txt:
		if ch == '-': res+=2

	print("Case #{0}: {1} ".format(it+1,res))
	w.write("Case #{0}: {1}\n".format(it+1,res))
w.close()