import math

def done(arr):
	count = 0
	for i in arr:
		if(i == 1):
			count += 1
	if(count == 10):
		return True
	else:
		return False

def evalNum(arr, num):
	if(num == 0):
		return
	else:
		endNum = int(num%10)
		num = int(math.floor((num)/10))
		arr[endNum] = 1
		evalNum(arr,num);

def lastNum(num):
	if(num == 0):
		return "INSOMNIA"
	else:
		arr = [0,0,0,0,0,0,0,0,0,0]
		multNum = 1
		number = num
		while(not done(arr)):
			number = num*multNum
			evalNum(arr, number)
			multNum += 1
		return number


if __name__ == "__main__":
	num = raw_input("enter num")
	lines = [line.rstrip('\n') for line in open('A-large.in')]
	count = 0
	f = open('output.txt', 'w')
	for string in lines:
		if(count != 0):
			f.write("Case #"+str(count)+": "+str(lastNum(int(string)))+"\n")
			print "Case #", count, ": ", lastNum(int(string))
		count += 1
	f.close()