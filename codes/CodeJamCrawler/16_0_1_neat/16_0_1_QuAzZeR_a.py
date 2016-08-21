
def check_digit(digit):
	for k in range(0,10):
		if digit[k] ==0:
			return False;
	return True

def main(k):
	a=(int)(input())
	i=1
	digit = [0,0,0,0,0,0,0,0,0,0]

	while True:
		temp = str(a*i)	
		for j in range(len(temp)):
			digit[(int)(temp[j])]+=1
		# print("a = "+temp+" "+str(digit))
		if check_digit(digit):
			print ("Case #"+str(k)+": "+temp)
			break
		if a == 0:
			print ("Case #"+str(k)+": INSOMNIA");
			break;
		i+=1

T = (int)(input())
for i in range(0,T):
	main(i+1)


