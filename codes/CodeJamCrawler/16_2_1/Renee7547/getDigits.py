import string
string.ascii_uppercase

filename = 'A-large.in'
with open(filename) as f:
	str_list = []
	case_num = f.readline().rstrip()
	str_list = [line.strip() for line in f]

n = {}
n[0] = "ZERO" #count z
n[1] = "ONE" #count[o] - 0 2 4
n[2] = "TWO" #count[W]
n[3] = "THREE" #count[t] - 2 8
n[4] = "FOUR" #count[r] - count[z]
n[5] = "FIVE" #count[f] - count[4]
n[6] = "SIX" #count[x]
n[7] = "SEVEN" #count[s] - count[x]
n[8] = "EIGHT" #count[g]
n[9] = "NINE" #count[i] - 5 6 8

#s = raw_input()
def check_num(s):
	num = []
	count = {}
	nc = {}
	for i in string.ascii_uppercase:
		count[i] = 0
	for c in s:
		count[c] += 1
	nc[0] = count['Z']
	for i in range(0, nc[0]):
		num.append(0);
	nc[2] = count['W']
	for i in range(0, nc[2]):
		num.append(2)
	nc[8] = count['G']
	for i in range(0, nc[8]):
		num.append(8)
	nc[4] = count['U']
	for i in range(0, nc[4]):
		num.append(4)
	nc[6] = count['X']
	for i in range(0, nc[6]):
		num.append(6)
	nc[3] = count['T'] - nc[2] - nc[8]
	for i in range(0, nc[3]):
		num.append(3)
	nc[7] = count['S'] - count['X']
	for i in range(0, nc[7]):
		num.append(7)
	nc[5] = count['F'] - nc[4]
	for i in range(0, nc[5]):
		num.append(5)
	nc[1] = count['O'] - nc[0] - nc[2] - nc[4]
	for i in range(0, nc[1]):
		num.append(1)
	nc[9] = count['I'] - nc[5] - nc[6] - nc[8]
	for i in range(0, nc[9]):
		num.append(9)
	num.sort()
	return num
output_file = 'output.txt'
output = open(output_file, 'w')
for i in range(0, int(case_num)):
	output.write("Case #%s: " % (i+1)) 
	s = str_list[i]
	num = check_num(s)
	for ele in num:
		output.write("%d" % ele)
	output.write("\n")
