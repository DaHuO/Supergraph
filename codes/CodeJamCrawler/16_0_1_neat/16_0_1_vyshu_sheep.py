#author: vysakh

N = 200;
numbers = [0, 1,  2,  3, 4, 5, 6, 7,8, 9]



i = 1

T = int(input());

inputs = []
for num in range(T):
	inputs.append(int(input()));


for i,n in enumerate(inputs):
	

	flag = False
	new_array = []
	if( n <= N):
		
		for j in range(1, N+1):
			num = n * j
			digits = [int(d) for d in str(num)]
			for digit in digits:
				if(digit not in new_array):
					new_array.append(digit)
					new_array.sort()
					if(numbers == new_array):
						flag = True
						print "Case #%d: %d " % (i+1, num)

		if(flag == False):
			print "Case #%d: %s " % (i+1, 'INSOMNIA')

	


			