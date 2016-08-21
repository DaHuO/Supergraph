import math
l = {}
coinstrlist = {}

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_prime_divisor(n):
    if n % 2 == 0 and n > 2: 
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return 0

def isJamCoin(coin):
	reslist = []
	baselist = [2,3,4,5,6,7,8,9,10]
	for base in baselist:
		converted = int(coin,base)
		if l[converted] is not None and l[converted] != 0:
			reslist.append(l[converted])
	return reslist

def prepare():
	n = 2
	baselist = [2,3,4,5,6,7,8,9,10]
	while n <=16:
		print n
		coinstrlist[n] = []
		c = 0
		for coin in jamcoiniterator(n):
			i = 0
			for base in baselist:
				value = int(coin,base)
				l[value] = is_prime_divisor(value)
				if l[value] != 0:
					i += 1
			if i == 9:
				c += 1
				print "C: {0}".format(c)
				coinstrlist[n].append(coin)
			if c == 50:
				break
		n += 1
	print "PREPARED"

def jamcoiniterator(n):
	if n == 2:
		yield "11"
		return
	formatstr = "1{0:0" + str(n-2) + "b}1"
	for x in range(2 ** (n-2)):
		yield formatstr.format(x)
	return

def solve(n, j, x, res):
	res.write("Case #{}:\n".format((x+1)))
	coinlist = coinstrlist[n]
	for coin in coinlist[:j]:
		b2 = l[int(coin,2)]
		b3 = l[int(coin,3)]
		b4 = l[int(coin,4)]
		b5 = l[int(coin,5)]
		b6 = l[int(coin,6)]
		b7 = l[int(coin,7)]
		b8 = l[int(coin,8)]
		b9 = l[int(coin,9)]
		b10 = l[int(coin,10)]
		res.write("{} {} {} {} {} {} {} {} {} {}\n".format(coin, b2, b3, b4, b5, b6, b7, b8, b9, b10))

def main():
	prepare()
	raw_input("Waiting")
	f = open("C://CodeJam/c.in", 'r')
	res = open("C://CodeJam/c.out", 'w')
	T = int(f.readline())
	for x in range(T):
		s = f.readline()
		ss = s.split()
		n = int(ss[0])
		j = int(ss[1])
		solve(n, j, x, res)
	f.close()
	res.close()	

if __name__ == "__main__":
	main()