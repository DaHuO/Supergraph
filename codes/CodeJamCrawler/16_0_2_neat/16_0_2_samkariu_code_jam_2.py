output = ""
with open("code_jam_test.txt") as f:
	N = f.next()
	line_num=1
	for line in f:
		line = line.strip()
		S = map(str,line)
		num_flips = 0
		prev_is_minus = False
		for i,C in enumerate(S):
			if C == '-':
				if i==0:
					num_flips+=1
				else:
					if prev_is_minus==False:
						num_flips+=2
				prev_is_minus = True
			else:
				prev_is_minus = False
		output+= 'CASE #'+str(line_num)+': '+str(num_flips) +'\n'
		line_num+=1
	f.close()

output = output.strip()
print output

with open("code_jam_test_output.txt","w") as r:
	r.write(output)
	r.close()
