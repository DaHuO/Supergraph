import sys

if __name__ == "__main__":
	filename = sys.argv[1]
	f = open(filename, 'r')
	lines = f.readlines()
	T = int(lines[0])
	ten = [0, 10,100,1000,10000,100000,1000000, 10000000]
	lenOfTen = len(ten)
	for i in range(0,T):
		num = int(lines[i+1])
		# print("num=%d" % (num))
		first = 0
		for j in range(0,lenOfTen-1):
			if num >= ten[j] and num < ten[j+1]:
				# print("ten[%d]=%d" % (j, ten[j]))
				if j == 0:
					first = num
				else:
					first = num / ten[j]

		if first == 0:
			print("Case #%d: INSOMNIA" % (i+1))
		else:
			mask = [0x200, 0x100, 0x80, 0x40, 0x20, 0x10, 0x8, 0x4, 0x2, 0x1]
			flag = 0b0000000000
			result = num
			j = 1
			while flag != 0b1111111111:
				new_num = num * j
				while new_num > 0:
					tmp = new_num / 10
					first_digit = new_num - tmp * 10
					new_num = tmp
					flag = flag | mask[first_digit]
					if flag == 0b1111111111:
						print("Case #%d: %d" % (i+1, num * j))
						break
				j = j + 1




