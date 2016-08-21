f = open('C-large.in', 'r')
g = open('C-large.out', 'w')
g.write("Case #1:\n")
import random
coin_list = []
coin_list2 = []

x = f.readline()
x = f.readline()
x = x.split()

n = int(x[0])
j = int(x[1])
#print(n, j)
#n = 32
while (len(coin_list2) < j):
#for cases in range(2):
	start = random.randint(2**(n-1) + 1, 2**n - 1)	
	rem = 0
	rem = (start%2)
	if(rem == 0):
		start = start + 1
	flag = 0
	for elements in coin_list:
		if elements == start:
			flag = 1
			break
	if (flag == 0):
		binary = bin(start)
		#print('this is the number, and in binary',start, binary)
		divisors = []
		for bases in range(2, 11):
			number = 0
			power = n-1
			for digits in binary[2:]:
				number = number + int(digits)*(bases**power)
				power = power - 1
			
			for i in range(2,100):
				if((number%i) == 0):
					#print(number, bases, i)
					divisors.append(i)
					break
		
		if(len(divisors) == 9):
			div_list = ''
			for element in divisors:
				div_list = div_list+str(element)+' '
			g.write((binary[2:])+' '+div_list+'\n')
			coin_list2.append(start)
	coin_list.append(start)
g.close()
