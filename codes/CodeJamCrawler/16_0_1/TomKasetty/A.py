num  = 0
num1 = 0
j = 0
for i in range(1, int(input())+1):

	num = int(input())
	digiset = set()
	j = 1
	while len(digiset) != 10 and num != 0:
		num1 = j*num
		j += 1
		temp = num1;
		while(temp != 0):
			digiset.add(temp%10)
			temp //= 10
		

	if len(digiset) == 10: print("CASE  #"+str(i) + ":",num1)
	else: print("CASE  #"+str(i) + ": INSOMNIA")