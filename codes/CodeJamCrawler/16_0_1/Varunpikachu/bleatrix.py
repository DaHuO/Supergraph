tcases=int(input())
case=1
def count_digits(num):
	
	if num==0:
		print('INSOMNIA')
		return
	digits_seen=[0]*10
	temp=num
	x=1
	while True:
		for dig in set(str(temp)):
			digits_seen[int(dig)]=1
			if all(digits_seen):
				print(temp)
				return
		temp=num*x
		x+=1
while case<=tcases:
	print('Case #'+str(case)+':',end=' ')
	num=int(input())
	count_digits(num)
	case+=1