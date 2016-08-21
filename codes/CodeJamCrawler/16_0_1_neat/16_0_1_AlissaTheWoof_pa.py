out =open('./paout.txt', 'w+')


t = int(input())
for x in range(0, t):
	numbers_not_seen = list(range(0, 10))
	original_number = int(input())
	if original_number == 0:
		out.write("Case #" + str(x+1) + ": "  + "INSOMNIA")
		out.write("\n")
	else:
		a = 1
		while (numbers_not_seen!=[]):
			current_number = [int(z) for z in str(original_number*a)]
			numbers_copy = [y for y in numbers_not_seen if (y not in current_number)]
			numbers_not_seen = numbers_copy
			a = a + 1
		out.write("Case #" + str(x+1) + ": " + ''.join(str(e) for e in current_number))
		out.write("\n")
out.close()