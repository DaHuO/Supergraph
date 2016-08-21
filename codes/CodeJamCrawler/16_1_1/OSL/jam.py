f = open("intput.txt", "r")
n = int(f.readline())

for k in range(n):
	s = f.readline()
	#print(s)
	prev = s[0]
	result = [s[0]]
	for i in range(1, len(s)):
		l = [s[i]] + result
		l = "".join(l)

		r = result + [s[i]]
		r = "".join(r)
		if l >= r:
			result = [s[i]] + result
			#print("more")
		else:
			result = result + [s[i]]
			#print("less", s[i])
		prev = s[i]
		if result[-1]=="\n":
			result[-1] = ""
	print("Case #" + str(k+1) + ": " + "".join(result))