import sys, itertools

def generate_coins(len):
	len -= 2
	coins = []
	coin_list = list(itertools.product([0, 1], repeat=len))
	for coin in coin_list:
		coin = "".join((str(coin).lstrip("(").rstrip(")").replace(" ", "")).split(","))
		coin = "1"+coin+"1"
		coins.append(coin)
	return coins

def is_prime(num):
	for i in range(2,int(num**0.5)+1):
		if num%i==0:
	    		return (False, i)
	return (True, 1)

def all_bases_non_prime(coin):
	is_all_non_prime = True
	divisors = []
	for i in range(2, 11):
		divisors.append("1")
		num = int(coin, i)
		(prime, divisor) = is_prime(num)
		if prime:
			is_all_non_prime = False
			break
		else:
			divisors[i-2] = str(divisor)
	return (is_all_non_prime, divisors)

def get_jam_coins(coins, num_coins):
	jam_coins = []
	count = 0
	for coin in coins:
		(non_prime, divisors) = all_bases_non_prime(coin)
		if non_prime:
			jam_coins.append((coin, divisors))
			count += 1
			if count == num_coins:
				break
	return jam_coins

def main():
	n = int(raw_input())

	for i in range(n):
		inp = raw_input()
		len = int(inp.split()[0])
		num_coins = int(inp.split()[1])
		
		coins = generate_coins(len)

		jam_coins = get_jam_coins(coins, num_coins)	
		print "Case #%d:" %(i+1)
		for jam_coin in jam_coins:
			print jam_coin[0] + " " + " ".join(jam_coin[1])

if __name__ == "__main__":
	main()
