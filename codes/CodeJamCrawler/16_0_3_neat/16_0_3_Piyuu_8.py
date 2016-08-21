import itertools
def is_prime(n):
	if n % 2 == 0:
		return 2
	if n%3 == 0:
		return 3
	f = 5
	while f*f <= n:
		if n%f == 0: return f
		if n%(f+2) == 0: return f+2
		f +=6
	return n   
str1='1'
flag=0
print("Case #1:")
for x in map(''.join, itertools.product('01',repeat=16)):
		ans_list = []
		for i in range(2, 11):
			z = int(str1+x+str1,i)
			y = is_prime(z)
			if(y != z):
				ans_list.append(y)
			else:
				break
		if len(ans_list) == 9:
			print(str1+x+str1,end=" ")
			[print(z, end=" ") for z in ans_list ] 
			print()
			flag = flag+1
			if flag==50:
				break
