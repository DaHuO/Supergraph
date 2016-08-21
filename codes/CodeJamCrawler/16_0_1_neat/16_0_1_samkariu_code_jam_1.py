output = ""
with open("code_jam_test.txt") as f:
	N = f.next()
	line_num=1
	for line in f:
		line = line.strip()
		digits = [0,1,2,3,4,5,6,7,8,9]
		num = int(line)
		if num==0:
			output+= 'CASE #'+str(line_num)+': INSOMNIA\n'
		else:
			num_tries = 1
			while len(digits) > 0:
				new_num = num_tries * num
				num_map = map(int, str(new_num))
				digits_set = set(digits).difference(num_map)
				digits = list(digits_set)
				if len(digits) == 0:
					output+= 'CASE #'+str(line_num)+': '+str(new_num) +'\n'
				num_tries+=1
		line_num+=1
	f.close()

output = output.strip()
print output

with open("code_jam_test_output.txt","w") as r:
	r.write(output)
	r.close()
