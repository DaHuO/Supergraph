n = int(input())

for j in range(n):
	s = input()
	count = 0
	for i in range(len(s)-1):
		if s[i]==s[i+1]:
			pass
		else:
			count+=1
	if s[len(s)-1] == '-':
		count+=1

	print("Case #"+str(j+1)+":" ,str(count))