def getDigits(num):
	digits=[]
	while num:
		digits.append(num%10)
		num/=10
	return digits

def main():
	T=input()

	for t in range(T):
		N=input()
		i=N
		if i==0:
			print "Case #"+str(t+1)+": INSOMNIA"
		else:
			whole_set=set()
			while 1:
				digits=getDigits(N)
				for digit in digits:
					whole_set.add(digit)
				if len(whole_set)==10:
					break
				N+=i
			print "Case #"+str(t+1)+": "+str(N)
if __name__=="__main__":
	main()