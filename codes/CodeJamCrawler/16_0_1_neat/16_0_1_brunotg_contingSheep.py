import io

digit_map = { }

def init_digits():
	for i in range(0,10):
		digit_map[i] = False

def read_data():
	test_data = {} #'number_lines':'', 'test_cases' : ''}
	test_data['test_cases'] = []
	file_name = 'A-large.in'
	f = open(file_name)
	n_cases = int (f.readline())
	test_data['number_lines'] = n_cases 
	for i in range(0, n_cases):  
		test_case = {}
		value = f.readline()
		test_case['initial_value'] = value
		test_data['test_cases'].append(test_case)
	return test_data

def print_values(val):
	for k in val.keys():
		print '%s-%s'%(k,val[k])

def are_all_digits_set():
	for k in digit_map.keys():
		if digit_map[k] != True:
			return False
	return True

def set_digits_flags(value):
	str_value = str(value)
	digits = map(int, list(str_value))
	for i in range(0, len(digits)):
		digit_map[digits[i]] = True
	#print_values(digit_map)

def process_data(test_data):
	count_samples = len(test_data['test_cases'])

''' receives a string value 
'''
def count_sheeps(value):
	value = value.strip() 
	if value == '0' : 
		return 'INSOMNIA'
	init_digits()
	
	int_value = int(value)
	set_digits_flags(value)
	all_set  = are_all_digits_set()
	count = 2
	while (all_set == False):
		#print 'value %s - flag %s' % (value, all_set)
		new_value = int_value * count 
		value = str(new_value)
		set_digits_flags(new_value)
		all_set  = are_all_digits_set()
		count += 1

	if all_set == True: 
		return value

def main(): 
	result_file_name = 'output.out'
	file_result = open(result_file_name, 'w')
	test_data = read_data()
	samples = len(test_data['test_cases'])
	test_cases = test_data['test_cases']
	line =  ''
	for i in range(0, samples): 
		extra = '\n' if i!= 99 else ''
		line = 'Case #%s: %s%s' % (i+1, count_sheeps(test_cases[i]['initial_value']), extra)  
		file_result.write(line)
	file_result.close()
if __name__ == "__main__": 
	main()