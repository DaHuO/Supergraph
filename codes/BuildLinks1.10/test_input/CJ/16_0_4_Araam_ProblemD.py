if __name__ == '__main__':
	with open('input2.txt', 'r') as f:
		with open('output2.txt', 'w') as o:
			lines_list = f.read().splitlines()[1:]
			for idx, lines in enumerate(lines_list):
				num_tiles, complexity, students = map(int, lines.split())
				if num_tiles > students:
					o.write("Case #{}: IMPOSSIBLE\n".format(idx + 1))
				else:
					total_tiles = int(pow(num_tiles, complexity))
					difference = total_tiles / students
					print(difference)
					a = list(range(1, students + 1))
					array = ' '.join([str(c) for c in a])
					o.write("Case #{}: {}\n".format(idx + 1, array))