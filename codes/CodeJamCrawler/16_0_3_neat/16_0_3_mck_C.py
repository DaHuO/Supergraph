import sys
from math import sqrt
from math import ceil

def isPrime(n):
	lim = sqrt(n) + 1;
	result = True
	
	if n % 2 == 0:
		result = False
	else:
		for i in range(3, ceil(lim), 2):
			if n % i == 0:
				result = False
				
	return result
	
def jamCoin(coin):
	c = [c for c in coin]
	ans = ""
	if c[-1] == "1" and c[0] == "1":
		for i in range(2, 11):
			if isPrime(int(coin, i)):
				return ""
					
		for i in range(2, 11):
			val = int(coin, i)
			div = -1
			for j in range(2, 10000):
				if val % j == 0 and j != val:
					div = j
					break
			if div != -1:
				if i == 10:
					ans += str(div)
				else:
					ans += str(div) + " "
			else:
				return ""
		return coin + " " + ans
	return ""
	
if __name__ == "__main__":
	tests = int(sys.stdin.readline())
	
	n, j = sys.stdin.readline().replace("\n", "").split(" ")
	
	val = ""
	for i in range(int(n)):
		val += "1"
	end = int(val, 2)
	val = ""
	for i in range(int(n)):
		if i == 0 or i == int(n) - 1:
			val += "1"
		else:
			val += "0"
	start = int(val, 2)
	
	print ("Case #1:")
	
	c = 0
	for i in range(start, end):
		result = jamCoin(bin(i).split("0b")[1])
		if result != "":
			c+= 1
			print(result)
		if c == int(j):
			break
