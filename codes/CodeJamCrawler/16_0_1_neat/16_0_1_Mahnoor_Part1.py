def countsheeps():
	input = open('A-large.in')
	test_cases = int(input.readline()) + 1
	# test_cases = test_cases 
	result_file = open('results.txt', 'w')

	for iterator in range(1,test_cases):
		check = ['0','1','2','3','4','5','6','7','8','9']	
		N = long(input.readline())
		if N != 0:
			count = 0
			x = 1
			number = 1
			while x:

				
				result = str(N*number)
				for result1 in result:
					if result1 in check:
						check[int(result1)] = True
				count = 0		
				for iter in range(0,10):
					if check[iter] == True: 
						count = count + 1
				if count == 10:
					break
				number = number + 1
					
			print >> result_file, "Case #%d: %s" % (iterator, result)
			
		else:
			print  >> result_file, "Case #%d: INSOMNIA" % (iterator)

if __name__ == "__main__":
	countsheeps()



