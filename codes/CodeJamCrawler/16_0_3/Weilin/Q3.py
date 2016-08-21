import numpy as np




def is_prime(number_10):
	square = int(np.sqrt(number_10)) + 1
	for i in range(2,square):
		if number_10 % i == 0:
			return False, i
	return True, i

def judge_jamcoin(number_10):
	number_2 = bin(number_10)[2:]
	number = list(np.zeros(9))
	divisor = []
	for i in range(9):
		number[i] = int(number_2, i + 2)
		[result, factor] = is_prime(number[i])
		if result:
			return 0, []
		else:
			divisor.append(factor)
	return 1, divisor



def jamcoins_single(N, J):
	string_base = '1' + '0' * (N-2) + '1'
	base_10 = int(string_base, 2)
	string_top = '1' + '1' * (N-2) + '1'
	top_10 = int(string_top, 2)
	number_10 = base_10
	to_print = [""]*J
	j = 0
	while(number_10 <= top_10 and j < J):
		[result, divisor] = judge_jamcoin(number_10)
		if result == 1:
			j += 1
			to_print[j-1] = bin(number_10)[2:] + " "
			for item in divisor:
				to_print[j-1] += str(item) + " "
			to_print[j-1] += "\n"
		number_10 += 2
	return to_print





f = open('C-small-attempt1.in')
r = f.read()
f.close()
whole_data = r.split('\n')
n = int(whole_data[0])

N = list(np.zeros(n))
J = list(np.zeros(n))

for i in range(1,n+1):
	N[i-1] = int(whole_data[i].split(' ')[0])
	J[i-1] = int(whole_data[i].split(' ')[1])



f_o = open('output.txt','w')
for i in range(n):
	f_o.writelines("Case #"+ str(i+1) + ":\n")
	to_print = jamcoins_single(N[i],J[i])
	for k in range(J[i]):
		f_o.write(to_print[k])
f_o.close()
