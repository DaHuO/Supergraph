def findans(N):
	if N == 0:
		return "INSOMNIA"

	num = N
	ans = 0
	digits = [0] * 10

	while 0 in digits:
		ans = ans + 1
		num = ans*N
		n = num
		while n:
			d = n%10
			digits[d] = 1
			n = n/10

	return num
	


def main():
	t = int(raw_input())
	f = open('output.txt', 'w')

	for i in range(0,t):
		N = int(raw_input())
		ans = findans(N)
		f.write("Case #"+str(i+1)+": "+str(ans)+"\n")
	
	f.close()

if __name__ == "__main__":
    main()