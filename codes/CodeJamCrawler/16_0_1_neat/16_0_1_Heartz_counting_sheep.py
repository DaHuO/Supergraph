test_cases = int(input())
for i in range(0,test_cases):
	n = int(input())
	if(n==0):
		print("Case #%d: INSOMNIA"%(i+1))
	else:
		digit_dict={}
		multiplier = 0
		while(len(digit_dict)<10):
			multiplier+=1
			list_of_digits = list(str(n*multiplier))
			for digit in list_of_digits:
				if digit not in digit_dict:
					digit_dict[digit]=1
		print("Case #%d: %d"%(i+1,n*multiplier))