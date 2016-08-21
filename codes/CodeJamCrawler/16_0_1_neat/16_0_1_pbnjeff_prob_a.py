digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def intersection(a, b):

	return list(set(a) & set(b))

with open('A-small-attempt3.in','r') as g:
	
	case = int(g.readline())
	case = 0
	
	with open('output_a.txt','w') as f:
	
		for line in g:
		
			case = case + 1
		
			if case > 100:
				break
			
			num = int(line)

			found = []

			i = 0

			if num is 0:

				f.write('Case #' + str(case) + ': INSOMNIA\n')

			else:
				
				while intersection(digits, found) != list(set(digits)):

					i = i + 1
					currentN = num * i
					
					for digit in str(currentN):
					
						if int(digit) not in found:
						
							found.append(int(digit))

				f.write('Case #' + str(case) + ': ' + str(currentN) + '\n')