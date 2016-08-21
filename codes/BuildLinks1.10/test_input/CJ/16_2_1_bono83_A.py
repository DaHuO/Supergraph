from copy import deepcopy


def initS(S):
	cc = {}
	for s in S:
		if s == '\n':
			continue
		if s in cc.keys():
			cc[s] += 1
		else:
			cc.update({
				s: 1
			})
	return cc

def phone_number(S):
	num_chars = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
	cc = initS(S)
	fail_num = []
	numchar = ""
	before = dict()
	while True:
		end = True
		wrong = True
		for k, v in cc.items():
			if k not in before.keys():
				wrong = False
			elif before[k] != v:
				wrong = False

			if v > 0:
				end = False
			if v < 0:
				fail_num.append(numchar)
				numchar = ""
				cc = initS(S)
				continue
		if wrong:
			fail_num.append(numchar)
			numchar = ""
			cc = initS(S)
			continue
		else:
			before = deepcopy(cc)

		if end:
			return''.join(sorted(numchar))

		if 'Z' in cc.keys() and cc['Z'] > 0 and check_fail(fail_num, numchar, 0):
			cc['Z'] -= 1
			cc['E'] -= 1
			cc['R'] -= 1
			cc['O'] -= 1
			numchar += '0'
		elif 'O' in cc.keys() and cc['O'] > 0 \
				and 'N' in cc.keys() and cc['N'] > 0 \
				and 'E' in cc.keys() and cc['E'] > 0 and check_fail(fail_num, numchar, 1):
			cc['O'] -= 1
			cc['N'] -= 1
			cc['E'] -= 1
			numchar += '1'
		elif 'W' in cc.keys() and cc['W'] > 0 and check_fail(fail_num, numchar, 2):
			cc['T'] -= 1
			cc['W'] -= 1
			cc['O'] -= 1
			numchar += '2'
		elif 'T' in cc.keys() and cc['T'] > 0 \
				and 'H' in cc.keys() and cc['H'] > 0 \
				and 'R' in cc.keys() and cc['R'] > 0 \
				and 'E' in cc.keys() and cc['E'] > 1 and check_fail(fail_num, numchar, 3):
			cc['T'] -= 1
			cc['H'] -= 1
			cc['R'] -= 1
			cc['E'] -= 2
			numchar += '3'
		# 4
		elif 'F' in cc.keys() and cc['F'] > 0 \
				and 'O' in cc.keys() and cc['O'] > 0 \
				and 'U' in cc.keys() and cc['U'] > 0 \
				and 'R' in cc.keys() and cc['R'] > 0 and check_fail(fail_num, numchar, 4):
			cc['F'] -= 1
			cc['O'] -= 1
			cc['U'] -= 1
			cc['R'] -= 1
			numchar += '4'

		# 5
		elif 'F' in cc.keys() and cc['F'] > 0 \
				and 'I' in cc.keys() and cc['I'] > 0 \
				and 'V' in cc.keys() and cc['V'] > 0 \
				and 'E' in cc.keys() and cc['E'] > 0 and check_fail(fail_num, numchar, 5):
			cc['F'] -= 1
			cc['I'] -= 1
			cc['V'] -= 1
			cc['E'] -= 1
			numchar += '5'
		elif 'X' in cc.keys() and cc['X'] > 0 and check_fail(fail_num, numchar, 6):
			cc['S'] -= 1
			cc['I'] -= 1
			cc['X'] -= 1
			numchar += '6'
		elif 'S' in cc.keys() and cc['S'] > 0 \
				and 'E' in cc.keys() and cc['E'] > 1 \
				and 'V' in cc.keys() and cc['V'] > 0 \
				and 'N' in cc.keys() and cc['N'] > 0 and check_fail(fail_num, numchar, 7):
			cc['S'] -= 1
			cc['E'] -= 2
			cc['V'] -= 1
			cc['N'] -= 1
			numchar += '7'
		elif 'G' in cc.keys() and cc['G'] > 0 and check_fail(fail_num, numchar, 8):
			cc['E'] -= 1
			cc['I'] -= 1
			cc['G'] -= 1
			cc['H'] -= 1
			cc['T'] -= 1
			numchar += '8'
		elif 'N' in cc.keys() and cc['N'] > 1 \
				and 'I' in cc.keys() and cc['I'] > 0 \
				and 'E' in cc.keys() and cc['E'] > 0 and check_fail(fail_num, numchar, 9):
			cc['N'] -= 2
			cc['I'] -= 1
			cc['E'] -= 1
			numchar += '9'




def check_fail(fail_num, numchar, add):
	if '{}{}'.format(numchar, add) in fail_num:
		fail_num.append(numchar)
		return False
	else:
		return True

# debug
# with open('/Users/blueshw/Documents/PycharmProjects/codejam/Round1-2/2/A/As.in') as f:
# 	t = int(f.readline())
# 	for i in range(1, t + 1):
# 		S = f.readline()
# 		print("Case #{}: {}".format(i, phone_number(S)))

# real
t = int(input())
for i in range(1, t + 1):
	S = input()
	print("Case #{}: {}".format(i, phone_number(S)))
