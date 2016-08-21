




def countSheep(N):
	digits = [0]*10;
	for i in range(1, 1000):
		number = N*i
		for j in range(len(str(number))-1, -1, -1):
			#print number
			digit = number / (10**j)
			digits[digit] = 1
			if sum(digits) == 10:
				#print i
				return N*i
			number = number % (10**j)
	print "no"
	return "INSOMNIA"







def main():
	fi = open("A-large.in","r")
	T = int(fi.readline())
	fo = open("output.txt","w")
	for i in range(T):
		N = int(fi.readline())
		result = countSheep(N)
		fo.write("Case #%i: %s\n"%(i+1,result))
	fi.close()
	fo.close()

main()