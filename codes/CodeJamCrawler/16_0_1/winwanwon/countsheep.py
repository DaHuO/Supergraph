loop = input()
res = 0
no = 1

while loop>0:
	num = raw_input()
	mul = 0
	all_digit_is_seen = 0
	loop_count = 1
	tup = ()
	while all_digit_is_seen==0 and loop_count<100:
		loop_count = loop_count + 1
		mul = mul+1
		num_mul = int(num)*int(mul)
		num_string = str(num_mul)
		digit = len(str(num_mul))
		i = 0
		while i<digit:
			tup = tup + (num_string[i],)
			i = i+1
			if ("0" in tup) and ("1" in tup) and ("2" in tup) and ("3" in tup) and ("4" in tup) and ("5" in tup) and ("6" in tup) and ("7" in tup) and ("8" in tup) and ("9" in tup):
				all_digit_is_seen = 1

	nos = str(no)
	ress = str(res)
	if all_digit_is_seen == 1:
		print 'Case #'+nos+': '+ num_string
	else:
		print 'Case #'+nos+': '+ "INSOMNIA"
	res = 0
	no = no+1
	loop = loop-1
