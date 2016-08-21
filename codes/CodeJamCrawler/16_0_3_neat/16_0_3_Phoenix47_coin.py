from math import sqrt;
from itertools import count, islice

def get_a_divisor(n, base, memo={}):
	num = int(n, base)
	if(num in memo):
		# print("memo hit")
		return memo[num]
	step = 0
	for i in islice(count(2), int(sqrt(num)-1)):
		step += 1
		if num % i == 0:
			memo[num] = i
			return i
		if (step > 10000):
			# give up
			break
	memo[num] = None
	return None

def validate_coin(n):
	proof = []
	for base in range(2,11):
		divisor = get_a_divisor(n, base)
		if (not divisor):
			return None
		proof.append(divisor)
	return (n, proof)

def generate_coin(n):
	ones = ''.join(map(str,[1] * (n-2)))
	f = "1{{:0{}b}}1".format(n-2)
	for i in range(int(ones,2) + 1):
		next_coin = f.format(i)
		yield next_coin

def make_jam_coins(n, j):
	results = []
	for i in generate_coin(n):
		coin = validate_coin(i)
		if (coin):
			# print (coin)
			results.append(coin)
			if(len(results) == j):
				break
	return results

if __name__ == "__main__":
	t = int(input())
	for i in range(1, t + 1):
		n, j = [int(s) for s in input().split(" ")]
		print("Case #{}:".format(i))
		for s in make_jam_coins(n,j):
			print(s[0], " ".join(map(str, s[1])))
