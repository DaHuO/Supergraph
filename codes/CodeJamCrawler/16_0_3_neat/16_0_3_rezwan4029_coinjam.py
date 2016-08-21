import math


primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def find_factor(n):
	for i in primes:
		if n % i == 0:
			return i
	return None

def get_divisors(binary):
    
	factors = []
    
	for b in range(2, 11):
		val = int(binary, b)
		factor = find_factor(val)
		if factor is None:
			break
		factors.append(factor)
		
	return factors

	
def get_coins(N, J):
    
	flag = 0
	ans = "Case #1:\n"
	size = 2**(N-2)
	cnt = -1
	while cnt < size:  
		cnt += 1
		binary = '1{}1'.format(format(cnt, '0{}b'.format(N-2)))
		
		divs = get_divisors(binary)
		
		if len(divs) == 9:
			flag += 1
			ans = ans + "{} {}".format(binary, " ".join(map(str, divs))) + "\n" 
		
		if flag == J:
			break
	
	return ans



if __name__ == "__main__":
    
	input = open("in.txt").read()

	input = input.split('\n')

	cs = int(input[0])

	n, j = map(int, input[1].split(' '))


	output = get_coins(n, j)
	
	with open("out.txt", 'w') as text_file:
		text_file.write(output[:-1])
