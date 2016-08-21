def solver(cases):
	with open("codejam-a-large.out", "w") as f:
		for i, c in enumerate(cases, start=1):
			f.write("Case #%d: %s\n" % (i, helper(int(c))))
		f.close()

def helper(num):
	digits = set([0,1,2,3,4,5,6,7,8,9])
	mult = 0
	if num == 0:
		return "INSOMNIA"
	while len(digits):
		mult += 1
		new_num = str(mult * num)
		for d in new_num:
			if int(d) in digits:
				digits.remove(int(d))
	return str(mult * num)

if __name__ == "__main__":
	with open('A-large.in', 'r') as f:
		f.readline()
		cases = f.readlines()
		solver(cases)
		f.close()
