def solution(S):
	if is_solution(S):
		return 0
	
	if is_next_solution(S):
		return 1

	pancakes_list = [S]
	operations_count = 0

	return search(pancakes_list, operations_count)

def search(pancakes_list, operations_count):
	pancakes_row = []
	operations_count += 1
	for pancakes in pancakes_list:		
		for i in range(len(pancakes)):
			pancakes_fliped = flip(pancakes, i + 1)

			if (is_solution(pancakes_fliped)):
				return operations_count
			if (is_next_solution(pancakes_fliped)):
				return operations_count + 1
				
			pancakes_row.append(pancakes_fliped)	
		
	return search(list(set(pancakes_row)), operations_count)

def flip(pancakes, flip_count):
	remaining_count = len(pancakes) - flip_count
	fliped = pancakes[0:flip_count][::-1].replace("+","m").replace("-","p").replace("p","+").replace("m", "-")
	
	if (remaining_count == 0):
		return fliped
		
	remaining = pancakes[-remaining_count:]
	return fliped + remaining

def is_solution(S):
	return len(set(S + "+")) == 1
	
def is_next_solution(S):
	return len(set(S + "-")) == 1	

if __name__ == "__main__":
	test_cases = input()
	for case in xrange(1, test_cases + 1):
		S = raw_input()  
		print "Case #%i: %s" %  (case, solution(S))
