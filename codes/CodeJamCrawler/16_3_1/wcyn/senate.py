import string
import heapq
filename = "A-small-attempt1(1)"
def get_digits(filename_in, filename_out):
	with open(filename_in, 'r') as input_f:
		test_cases = int(input_f.readline());
		for x in range(test_cases):
			parties = string.ascii_uppercase[:int(input_f.readline().replace('\n',''))]
			numbers = list(input_f.readline().replace('\n','').replace(' ',''))
			numbers = [int(i) for i in numbers]
			strategy = []
			print(parties)
			print(numbers)
			while sum(numbers) > 0:
				if len(set(numbers)) == 1:
					if len(numbers)%2 !=0:
						# print("similar")
						strategy.append(parties[0])
						numbers[0]-=1
					else: 
						strategy.append(parties[0] + parties[1])
						numbers[1]-=1
						numbers[0]-=1
				else:
					most = heapq.nlargest(2, numbers)
					# print("most:", most)
					if len(set(most)) == 1:
						indices = [i for i, j in enumerate(numbers) if j == most[0]]
						strategy.append(parties[indices[0]] + parties[indices[1]])
						numbers[indices[1]]-=1
						numbers[indices[0]]-=1
					else:
						strategy.append(parties[numbers.index(most[0])] + parties[numbers.index(most[1])])
						# print("numbers before:",numbers)
						numbers[numbers.index(most[1])]-=1
						numbers[numbers.index(most[0])]-=1
						# print("numbers after:",numbers)
				# print("strategy in:", strategy)
				# print(parties)
				# print(numbers)
			print("strategy:", strategy)
			mode = 'a'         
			with open(filename_out,mode) as output_f:
			    output_f.write('Case #%d: %s\n' %(x+1, " ".join(strategy)))
get_digits(filename + '.in', filename + '.out')