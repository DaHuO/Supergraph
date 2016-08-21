f = open("input", "r")
o = open("output", "w")
n = int(f.readline())
for x in range(n):
	m = f.readline()[:-1]
	if m.count("-") == len(m) or m.count("+") == len(m):
		o.write("Case #" + str(x+1) + ": " + ("1" if m[0] == "-" else "0") + "\n")
		continue
	
	flip = 0
	for i in range(1, len(m)):
		if m[i] != m[i-1]:
			flip += 1

	if (flip % 2 == 0 and m[0] == "-") or (flip % 2 == 1 and m[0] == "+"):
		flip += 1

	line = str(flip)
	o.write("Case #" + str(x+1) + ": " + str(line) + "\n")
o.close()
f.close()
