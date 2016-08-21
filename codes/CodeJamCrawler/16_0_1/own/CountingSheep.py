
s_check = set()
s_check.add(0)
s_check.add(1)
s_check.add(2)
s_check.add(3)
s_check.add(4)
s_check.add(5)
s_check.add(6)
s_check.add(7)
s_check.add(8)
s_check.add(9)
c = input()

def N(num):
	s = set()
	def enter_numbers(num,s):
		str_num = str(num)
		for i in range(0,len(str_num)):
			s.add(int(str_num[i]))

	i=1
	while s!=s_check:
		enter_numbers(num*i,s)
		i = i+1

	return  (i-1,num*(i-1))
	

for i in range (1,c+1):
	num = input()
	if num!=0:
		print 'Case #{i}: {num}'.format(i=i,num=N(num)[1])
	else:
		print 'Case #{i}: INSOMNIA'.format(i=i)