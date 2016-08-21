'''
=================================================
   Author : Rohit Sharma
   Handle : skyrohithigh
   Heritage Institute of Technology
   Problem : Coin Jam
   Contest : CodeJam16
   Website : Google
   Date : 09/04/2016
=================================================
'''

def get_coin(n):
	s = "0"*(n-2)
	return "1"+s+"1"

def next_coin(n):
	coin = int(n,2)
	coin = coin + 2
	return bin(coin)[2:]

def first_nontrival_divisor(n):
	for i in range(2, 1000):
		if n % i == 0:
			return i
	return -1

def main():
	T = int(input())
	for t in range(1,T+1):
		print("Case #"+ str(t) +": ")
		n, j = map(int, input().split(' '))
		coin = get_coin(n)
		while j > 0:
			ans = ""
			flag = True
			for b in range(2,11):
				divisor = first_nontrival_divisor(int(coin, b))
				if divisor == -1:
					flag = False
					break
				else:
					ans = ans + " "+str(divisor)
			if flag:
				print(coin+" "+ans)
				j = j - 1
			coin = next_coin(coin)	
			
if __name__ == "__main__":
	main()