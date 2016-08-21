import itertools
test = int(input())
for k in range(test):
	string = input()
	a = string[0]
	for i in range(1,len(string)):
		if(a[0] <= string[i]):
			a = string[i]+a
		else:
			a = a+string[i]
	print("Case #",k+1,": ", a, sep = '')
