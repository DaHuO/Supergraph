def count_sheep(N, digits, mult=1):
	if N == 0:
		return "INSOMNIA"
	for digit in str(N*mult):
		if digit in digits:
			del digits[digit]
	if len(digits) == 0:
		return N * mult
	else:
		return count_sheep(N, digits, mult + 1)



if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(1, testcases+1):
		digits = {"0":None, "1":None, "2":None, "3":None, "4":None, "5":None, "6":None, "7":None, "8":None, "9":None}
		N = raw_input()
		print("Case #%i: %s" % (caseNr, count_sheep(int(N), digits)))