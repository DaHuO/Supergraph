lines = open('A-small-attempt0.in', 'r').readlines()
cases = int(lines[0])

s = ''
for case in range(cases):
	num = int(lines[case+1])
	if num == 0:
		s += "Case #%s: INSOMNIA\n" %  (case+1)
		continue
	elif num < 0 or num > 1000000:
		s += "Input out of range\n"
		continue
	nums = set("0123456789")
	mult = 0
	while True:
		mult += num
		nums = nums - set(str(mult))
		if len(nums) == 0:
			s += "Case #%s: %s\n" % (case+1, mult)
			break
with open("out.txt", "w") as outf:
	outf.write(s)