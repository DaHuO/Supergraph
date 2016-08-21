
nb_entry = int(input())

for i in range(1, nb_entry+1):
	out = "Case #"+str(i)+': '
	pan = raw_input()
	prev = pan[0]
	total = 0
	if prev == '-':
		total = 1
	for c in pan:
		if c==prev:
			continue
		else:
			if prev=='+' and c =='-':
				total+=2
		prev = c
	
	out +=str(total)
	print(out) 
