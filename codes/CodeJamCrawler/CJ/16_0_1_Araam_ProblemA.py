if __name__ == '__main__':
	with open('input.txt', 'rb') as f:
		with open('output.txt', 'w') as o:
			lines_list = f.readlines()[1:]
			for idx, line in enumerate(lines_list):
				num = int(line)
				base_num = num
				a = [0] * 10
				char_count = len(str(num))
				max_num = int(str(num) + "0" * (char_count * 3))
				while sum(a) != 10 and num != 0:
					str_num = str(num)
					for number in str_num:
						a[int(number)] = 1
					num += base_num
				if sum(a) != 10:
					o.write("CASE #{}: INSOMNIA\n".format(idx + 1))
				else:
					o.write("CASE #{}: {}\n".format( idx + 1, num - base_num))