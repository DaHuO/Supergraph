import sys

input_list = []
output_list = []

try:
	input_filename = sys.argv[1]
	output_filename = input_filename[:sys.argv[1].find('.')]+'.out'
except:
	print 'input filename as argv'
	exit()

try:
	input_f = open("./"+input_filename)
	input_lines = input_f.readlines()
	input_count = 0
	for input_line in input_lines:
		if input_count %2 == 0:
			input_split = input_line.split()
			input_split = map(int, input_split)
			input_list.append(input_split)
		# input_list.append(input_line.strip())
		input_count += 1
	input_f.close()
except:
	print 'read error'
	exit()

input_list.pop(0)
alphabet_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_R(input_item):
	#print 'init', input_item
	#exit()
	if sum(input_item) == 2:
		for x in range(len(input_item)):
			if input_item[x] == 1:
				for y in range(x+1,len(input_item)):
					if input_item[y] == 1:
						return alphabet_str[x]+alphabet_str[y]
	else:
		if input_item.count(max(input_item)) == 1 or max(input_item) == 1:
			input_item2 = input_item[:]
			input_item2[input_item.index(max(input_item))] -= 1
			#print 'A', input_item2
			#exit()
			return alphabet_str[input_item.index(max(input_item))] + ' ' + get_R(input_item2)
		else:
			#print 'B', input_item
			#exit()
			x = input_item.index(max(input_item))
			input_item2 = input_item[:]
			input_item2[x] -= 1
			y = input_item2.index(max(input_item2))
			input_item2[y] -= 1
			#print x, y, input_item2
			#exit()
			return alphabet_str[x] + alphabet_str[y] + ' ' + get_R(input_item2)
	pass

for input_item in input_list:

	# do some works here
	
	result = get_R(input_item)
	result += ''
	output_list.append([result])

try:
	output_f = open("./"+output_filename, "w")
	output_f.close()
except:
	pass

try:
	output_f = open("./"+output_filename, "a")
	output_str = ''

	for x in range(len(output_list)):
		output_f.write('Case #' + str(x+1)+': '+str(output_list[x][0])+"\n")
		print x
	output_f.close()
except:
	print 'write error'
	exit()
