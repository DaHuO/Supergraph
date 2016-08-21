
def number2list(n):
	return [int(i) for i in str(n)]

for t in range(input()):
	n = input()
	dict_digit = dict()
	multiplier = 1

	while len(dict_digit) < 10 and n > 0:
		mul_n = n*multiplier
		list_n = number2list(mul_n)
		#print list_n

		for i in list_n:
			dict_digit[i]=1
		#print dict_digit
		#print len(dict_digit)
		multiplier+=1

	if len(dict_digit) < 10:
		mul_n = "INSOMNIA"

	print "Case #%d: %s" %(t+1,mul_n)
