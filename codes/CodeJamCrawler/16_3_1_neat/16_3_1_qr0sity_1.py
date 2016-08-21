cases = int(input())

def findmax(dict, set_char):
	max = 0
	max2 = 0
	maxc = '0'
	max2c = '0'
	total = 0
	for c in set_char:
		if c in dict:
			if dict[c] > max:
				max = dict[c]
				maxc = c
			total += dict[c]
	for c in set_char:
		if c in dict:
			if dict[c] > max2 and c != maxc and abs(dict[c] - max) <= 1 and total != 3:
				max2 = dict[c]
				max2c = c
	if maxc in dict:
		dict[maxc] -= 1
	if max2c in dict:
		dict[max2c] -= 1
	return maxc, max2c

import string
to_char = dict(enumerate(string.ascii_lowercase, 1))

strs = []
setc = []
for case in range(cases):
	n = int(input())
	number = 1
	raw_strs = input().split(' ')
	strs_temp = ""
	setc_temp = []
	for st in raw_strs:
		sumc = int(st)
		for i in range(sumc):
			strs_temp += to_char[number]
		setc_temp.append(to_char[number])
		number += 1
	strs.append(strs_temp)
	setc.append(setc_temp)

for case in range(cases):
	dict = {}
	for c in strs[case]:
		if c not in dict:
			dict[c] = 1
		else:
			dict[c] += 1
	res = []
	while True:
		max1, max2 = findmax(dict, setc[case])
		res_str = ""
		if max1 != '0':
			res_str += max1
		if max2 != '0':
			res_str += max2
		if res_str == "":
			break
		res.append(res_str)
	print_res = str(" ".join(map(str, res)))
	print_res = print_res.upper()
	print("Case #%d: %s" % (case+1, print_res))

