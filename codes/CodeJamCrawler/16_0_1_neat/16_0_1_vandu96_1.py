test = int(input())
for i in range(test):
	num = int(input())
	org = num
	count = 1
	arr = []
	if(num == 0):
		print("Case #", i+1, ": ", "INSOMNIA", sep = "")
	else:
		while(len(arr) < 10):
			num = org * count
			num1 = set(str(num))
			for j in num1:
				if j not in arr:
					arr.append(j)
			count = count + 1
			
		print("Case #", i+1, ": ", num, sep = "")
		
