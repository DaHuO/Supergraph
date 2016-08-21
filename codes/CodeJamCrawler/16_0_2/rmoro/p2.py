###
## Robert Morouney
## moro1422@mylaurier.ca
## Friday April 08 2016
##
## Google_Code Jam Qualify_B: Revenge of the Pancakes
##

fout = open('B-large.out', 'w')
fin = open('B-large.in', 'r')
cases = 0
case = 0

for line in fin:

	idx = 0
	iterations = 0
	stack = list(line.strip())
	flips = 0
	test = ["+", "-"]
	done1 = '+' * len(stack)
	done2 = '-' * len(stack)

	if cases == 0: cases = int(line.strip())
	elif case > cases: break
	else:
		case = case + 1
		t_stack = ''.join(c for c in stack)
		while t_stack != done1 and t_stack != done2:
			idx = 0
			while (idx < len(stack) and stack[idx] != test[iterations%2]):
				idx += 1
					
			if idx != 0:
				for i in range(idx):
					stack[i] = test[iterations%2]
				flips = flips + 1
			
			iterations += 1
			t_stack = ''.join(c for c in stack)
			
		if t_stack == done2 : flips = flips + 1
		fout.write("Case #{0}: {1}\n".format(case, flips))
##### 
		print "Case #{0}: {1}".format(case, flips) 
#####				

fout.close()
fin.close()
