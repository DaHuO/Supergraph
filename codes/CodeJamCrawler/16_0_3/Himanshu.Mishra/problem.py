def isprime(n):
	if n == 2:
		return True
	if not n & 1:
		return False
	return pow(2, n-1, n) == 1


# def isprime(n):
#     """Returns True if n is prime."""
#     if n == 2:
#         return True
#     if n == 3:
#         return True
#     if n % 2 == 0:
#         return False
#     if n % 3 == 0:
#         return False

#     i = 5
#     w = 2

#     while i * i <= n:
#         if n % i == 0:
#             return False

#         i += w
#         w = 6 - w

#     return True

def isDivisibleBy(num):
	for i in range(2, num):
		if num%i==0:
			return i


def main():
	data =  []
	print("Case #1:")
	for i in range(35):
		num = 2**i
		# print(num, len(bin(num)[2:]), bin(num+1)[2:], bin(int(num*2-1))[2:])
		data.append([num+1, int(num*2-1)])

	N = 32
	count = 0
	startingNumber = data[N-1][0]
	finalNumber = data[N-1][1]

	for i in range(startingNumber, finalNumber+1, 2):
		numstr =  bin(i)[2:]
		base = [int(numstr, 2), int(numstr, 3), int(numstr, 4), int(numstr, 5), int(numstr, 6), int(numstr, 7), int(numstr, 8), int(numstr, 9), int(numstr, 10)]
		# print(base)
		flag = 0
		for j in base:
			if not isprime(j):
				flag = 1
			else:
				flag = 0
				break
		if flag == 1:
			if count >= 700:
				break
			else:
				count =  count + 1
			answer = str(base[10-2])
			for k in base:
				answer += " " + str(isDivisibleBy(k))
			print(answer)

if __name__ == '__main__':
	main()