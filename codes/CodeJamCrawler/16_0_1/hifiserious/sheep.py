def getAllDigits (n):
	missing_digits = ["0" , "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	cur_n = n
	i = 0
	if n == 0:
		return "INSOMNIA"
	else:
		while (len(missing_digits) > 0):
			i += 1
			cur_n = n * i
			number_str = str(cur_n)
			new_missing_digits = missing_digits[:]
			for x in missing_digits:
				if x in number_str:
					new_missing_digits.remove(x)
			missing_digits = new_missing_digits[:]
		return cur_n




t = int(raw_input()) 
for i in xrange(1, t + 1):
   n = int(raw_input())
   print "Case #{}: {}".format(i, getAllDigits(n))
