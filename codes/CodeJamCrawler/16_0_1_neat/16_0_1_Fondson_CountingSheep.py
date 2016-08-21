t = int(input())
for i in range(1, t + 1):
	digits=['0','1','2','3','4','5','6','7','8','9']  
	count=0
	num=list(input())
	if num!=['0']:
		while len(digits)!=0:
			if count!=0:
				num=list(str(int(''.join(num))//count))
			count+=1
			num=list(str(int(''.join(num))*count))
			for j in range(len(num)):
				if num[j] in digits:
					digits.remove(num[j])
		print ("Case #{}: {}".format(i, ''.join(num)))
	else:
		print ('Case #{}: {}'.format(i,'INSOMNIA'))