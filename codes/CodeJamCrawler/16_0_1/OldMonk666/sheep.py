
w = open("output_sheep.out", "wb")
with open("A-large.in","rb") as fd:
	val = int(fd.readline())
	
	for j in range(val):
		dig = fd.readline()
		set_digits = set()
		for digits in dig:
			if digits == '\n':
				pass
			else:
				set_digits.add(digits)
		dig_int = int(dig)
		if dig_int == 0:
			w.write("Case #" + str(j+1) + ":" + " INSOMNIA\n")
		else:
			i = 1
			temp = dig_int
			while len(set_digits) < 10:
				temp = dig_int * i
				temp_str = str(temp)
				i = i + 1
				for digits in temp_str:
					set_digits.add(digits)
				if i > 10000:
					print "Currently iterating", dig_int
			w.write("Case #" + str(j+1) + ": " + str(temp) + "\n")
			
		
