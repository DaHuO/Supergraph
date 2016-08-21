import re
t = int(raw_input())
for i in range(1,t+1):
	str1 = "Case #"+str(i)+": "
	x = raw_input()
	y = ""
	for i in x:
		if i == '+':
			y+=str(1)
		else:
			y+=str(0)
	flag = False
	if y[-1] == '1':
		flag = True
	z = [m.group(0) for m in re.finditer(r"(\d)\1*", y)]
	
	ans = len(z)
	if flag == True:
		ans-=1
	str1+=str(ans)
	print str1