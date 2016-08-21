def isPrime(num):
	for i in range(2,int(num**0.5) + 1):
		if num % i == 0:
			return False
	return True




def convertBiToBase(jamcoin):
	list_ = []
	num = jamcoin
	for i in range(2,11):
		tmp = num
		result = 0
		j = 0
		while tmp != 0:
			digit = tmp % 10
			result += digit * pow(i,j)
			tmp = tmp // 10
			j += 1
		if(isPrime(result)):
			return list()

		list_.append(result)

	return list_		



def findDivider(num):
	for x in num:
		for i in range(2,x):
			if x % i == 0:
				print(i,end=' ')
				break
	print()

def coin_jam_generate(length,j,count):
    for i in range(pow(2, length-2)):
    	if count == j:
    	   break
    	else:
        	coin = pow(10, length - 1) + int("{0:b}".format(i)) * 10 + 1
        	list_ = convertBiToBase(coin)
        	if list_ != []:
	        	print(coin,end=' ')
	        	findDivider(list_)
	        	count += 1


t = int(input())
tmp = input().split()
n = int(tmp[0])
j = int(tmp[1])

if (t == 1):
	print('CASE #1:')
	count = 0
	coin_jam_generate(n,j,count)



