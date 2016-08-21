import random
T = 0
m = 1
my_num = 0
dig = []

def num_to_dig_list(num, dig):
	while num > 9:
                if num % 10 not in dig:
                        dig.append(num % 10)
                num /= 10
        if num % 10 not in dig: 
                dig.append(num)
        # print dig

def sleeping_time(case_num, num):
	global m, dig
	num_to_dig_list(num, dig)
	if num == 0:
		print 'Case #%d: INSOMNIA' % (case_num + 1)
		m = 1
		dig = []
		return
	if len(dig) != 10:
		m += 1
		sleeping_time(case_num, m*my_num)
		# num_to_dig_list(m*num, dig)
	else:
		print 'Case #%d: %d' % (case_num + 1, m*my_num)
		m = 1
		dig = []

T = input()
for case_num in range(T):
    num = input()
    my_num = num
    sleeping_time(case_num, num)
