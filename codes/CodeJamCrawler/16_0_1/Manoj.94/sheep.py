
f = open("input","r+")
o = open("output","w+")
line = f.readlines()
for i in range(int(line[0])):
	num = int(line[i+1])
	if num == 0:
		o.write("Case #%d: INSOMNIA\n" % (i+1))
	else:
		N = 1
		flag = False
		arr = [0] * 10
		while True:
			val = num * N
			for digit in str(val):
				arr[int(digit)] = 1
			if all(arr):
				o.write("Case #%d: %s\n" % (i+1,val))
				break
			N = N + 1
f.close()
o.close()
