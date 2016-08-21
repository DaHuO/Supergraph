import itertools

def is_prime(n):
	n*=1.0
	for divisor in range(2,int(int(n**0.5)**0.5)+1):
		if n/divisor==int(n/divisor):
			return "False" + " " + str(divisor)
	return "True"

file_to_read = open('C-small-attempt2.in','r')
file_to_write = open('output.txt','w')
content = file_to_read.read().splitlines()
n = content[1].split()[0]
j = content[1].split()[1]
# allpossible = [''.join(i) for i in itertools.product("01",repeat=int(n)) if i[0] == '1' and i[-1] == '1']
# print allpossible
count2 = 0
file_to_write.write("Case #1:\n")
for string in itertools.product("01",repeat=int(n)):
	if string[0] == '1' and string[-1] == '1':
		string = ''.join(string)
		print string	
		numbers = []
		divisors = []
		count = 0
		for i in range(2,11):
			numbers.append(int(string,i))
		for b in numbers:
			if is_prime(b).split()[0] == "False":
				divisors.append(is_prime(b).split()[1])
				count = count + 1
		if count == 9:
			result = ""
			if count2 == int(j):
				break
			count2 = count2+1
			result += string+" "
			for m in range(len(numbers)):
				result += str(divisors[m])+" "
			file_to_write.write(result+'\n')  