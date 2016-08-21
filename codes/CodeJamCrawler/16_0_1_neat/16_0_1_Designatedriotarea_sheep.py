import sys
t = int(raw_input())
for i in range(1, t+1):
	clock = 0
	check = set(["0", "1" , "2", "3", "4","5", "6", "7", "8", "9"])
	inpt = str(raw_input())
	num = inpt
	if num == "0": num = "INSOMNIA" 
	while num != "INSOMNIA":
		for digit in num: 
			if digit in check: check.remove(digit)
		if check == set([]):
			break
		num = str(int(inpt) * (2 + clock))
		clock += 1
	print("Case #{}: {}".format(i, num))

