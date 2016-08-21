t = eval(input())
yo = 1
arr = list()
for i in range(10):
	arr.append(i)

def set(n):
	while(n != 0):
		arr[n % 10] = 1
		n = int(n / 10)
		
def check():
	for i in range(10):
		if arr[i] == 0:
			return False
	return True
	
while yo <= t:
	n = eval(input())
	if(n == 0):
		print("Case #", yo,": INSOMNIA", sep="")
		yo += 1
		continue
	#Initialising the array with 0s
	for i in range(10):
		arr[i] = 0
	
	count = 2
	temp = n
	
	while True:
		set(temp)
		if(check()):
			break
		temp = count * n
		count += 1
	
	print("Case #", yo, ": ", temp, sep="")
	yo += 1
