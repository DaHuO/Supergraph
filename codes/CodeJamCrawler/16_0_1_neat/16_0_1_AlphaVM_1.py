# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
u= int(input())  # read a line with a single integer
for i in range(1, u + 1):
	t = input() # read a list of integers, 2 in this case
	#print("Case #{}: {} {}".format(i, n + m, n * m))
	# check out .format's specification for more formatting options
	if t==0:
		print("Case #{}: {}".format(i, "INSOMNIA"))
	#fileo.write(s+"\n")
		continue
	else:
		h=set(str(t))
		o=2;
		k=0
		while len(h)<10:
			k=t*o
			h=h|set(str(k))
			o+=1
	#print s
		print("Case #{}: {}".format(i, k))
	#fileo.write(s+"\n")
