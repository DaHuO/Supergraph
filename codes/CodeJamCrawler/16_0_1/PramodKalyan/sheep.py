n = int(input())
a = [0,1,2,3,4,5,6,7,8,9] 
k = []

temp = 0
for i in range(n):
	num = int(input())
	temp1 = num
	k=[]
	l = 1;
	while k != a and num != temp :
		#print("hello")
		
		string = list(str(num))
		for j in string:
			if int(j) not in k:
				k.append(int(j))
				k.sort()
		l = l+1
		#print(num)
		#print(k)
		temp = num
		num = l*temp1
	if(num==temp):
		print("case #",end="")
		print(i+1,end="")
		print(": INSOMNIA")
	else:
		print("case #",end="")
		print(i+1,end="")
		print(":",temp)	
		
