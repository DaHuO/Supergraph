#! /usr/bin/python

def solve(n):
	found = [False]*10
	count = 0
	solution = 0
	while count<10:
		solution += n
		x = solution
		while x!=0:
			d = x%10
			x /= 10
			if not found[d]:
				found[d] = True
				count += 1
	return solution

def main():
	t = int(raw_input())
	for i in range(1, t+1):
		n = int(raw_input())
		if n==0:
			print("Case #%d: INSOMNIA" % i)
		else:
			print("Case #%d: %d" % (i, solve(n)))

if __name__=="__main__":
	main()