def main():
	num_of_test = int(input())

	for test_id in range(1, num_of_test + 1):
		k, c, s = (int(i) for i in input().split())
		print("Case #" + str(test_id) + ":", end="")
		for i in range(1, k+1):
			print(" " + str(i), end="")
		print()

if __name__ == "__main__":
	main()
