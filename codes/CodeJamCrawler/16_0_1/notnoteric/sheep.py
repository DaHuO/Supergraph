
def main():
	with open("sheep.in") as f:
		n = int(f.readline().strip())

		for case in range(1, n+1):

			num = int(f.readline().strip())
			ans = count_sheep(num)
			print("Case #{case}: {ans}".format(**locals()))

def count_sheep(n):
	if n == 0:
		return "INSOMNIA"

	nums = set([])
	i = 1

	while True:
		num = n * i

		for digit in get_digits(num):

			if digit not in nums:
				nums.add(digit)
				if len(nums) == 10:
					return num
					
		i += 1

def get_digits(n):
	while n:
		yield n % 10
		n = n // 10

if __name__ == "__main__":
	main()
