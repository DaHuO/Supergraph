def get_digits(i):
	dic = {}
	while(i != 0):
		dic[i%10] = 1
		i = i/10
	return dic

def add_digits(dic1, dic2):
	for k in dic2:
		dic[k] = 1


T = int(raw_input())

output_template = 'Case #'

for i in range(1,T+1):
	inp = int(raw_input())
	if inp == 0:
		print output_template + str(i) + ': INSOMNIA'
	else:
		dic = {}
		j = 1
		while(True):
			add_digits(dic, get_digits(inp*j))
			if(len(dic) == 10):
				print output_template + str(i) + ': ' + str(inp*j)
				break
			j += 1 