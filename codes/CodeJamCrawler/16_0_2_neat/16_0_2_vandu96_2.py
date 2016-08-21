test = int(input())
for t in range(test):
	count = 0
	string = list(input())
	org = "".join(string)
	i = len(string)-1
	while(i >= 0):
		while( i >= 0 and string[i] != "-"):
			i = i-1
		if(i != -1):
			for j in range(i+1):
				if(string[j] == "+"):
					string[j] = '-'
				else:
					string[j] = '+'
			count = count + 1
		i = i-1
	print("Case #",t+1,": ", count, sep = "")
