def swap(L):
	for i in range(len(L)):
		if L[i] == '+':
			L[i] = '-'
		else:
			L[i] = '+'
	return L
		
def flip(pan, p):
	if pan[0] == '+':
		while pan[p-1] == '-':
			p = p-1
		temp = pan[0:p]
		temp.reverse()
		temp = swap(temp)
		temp.extend(pan[p:len(pan)])
	else:
		temp = pan[0:p+1]
		temp.reverse()
		temp = swap(temp)
		temp.extend(pan[p+1:len(pan)])
	return temp
	
def validate(panStack, t):
	pos = -1
	for i in range(len(panStack)):
		if panStack[i] == '-':
			pos = i
	if pos != -1:
		panStack = flip(panStack, pos)
	return panStack	

tc = int(input())
for i in range(1, tc+1):
	panStack = list(input())
	N = 0
	while '-' in panStack:
		panStack = validate(panStack, i)
		N += 1
	print("Case #{}: {}".format(i, N))
