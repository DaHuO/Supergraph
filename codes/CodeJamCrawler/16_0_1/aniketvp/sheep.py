def get_num(i):

	orig = i
	digits = set()
	numbers = set()
	count = 1
	while i not in numbers:
		numbers.add(i)
		digits = digits.union(set(str(i)))
		if len(digits) == 10:
			return i
		count += 1
		i = orig*count
	return "INSOMNIA"


def main():
	n = input()

	f = open("output.txt",'w')
	for i in range(n):

		f.write("Case #" + str(i+1) + ": " + str(get_num(input()))+"\n")
	f.close()

if __name__=="__main__":
	main()