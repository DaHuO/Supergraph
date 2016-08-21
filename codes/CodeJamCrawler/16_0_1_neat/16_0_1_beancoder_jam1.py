T = int(raw_input())
input_list = []
for i in range(T):
	input_list.append(int(raw_input()))

case_number = 0
for number in input_list:
	case_number += 1;
	if(number == 0):
		print "Case #"+str(case_number)+": INSOMNIA"
	else:
		digit_list = []
		multiplier = 0
		init = number
		while len(digit_list)!=10:
			multiplier += 1
			num = init*multiplier
			str_num = str(num)
			for i in str_num:
				if i not in digit_list:
					digit_list.append(i)
		print "Case #"+str(case_number)+": "+str_num