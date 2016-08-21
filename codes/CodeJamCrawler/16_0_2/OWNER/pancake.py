t = int(input())

for i in range(t):
	pancake = list(raw_input())
	count =0;
	if pancake[0]=='-':
		count = count + 1
	for j in range(1, len(pancake)):
		if pancake[j-1]=='+' and pancake[j]=='-':
			count = count + 2
	string = "Case #"+str(i+1)+": "+str(count)
	print string