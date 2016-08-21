




if __name__ == "__main__":
	with open('A-large.in', 'r') as f:
		with open('aout.txt', 'w') as aout:
			cases = int(f.readline().rstrip())
			case = 1
			for s in f.readlines():
				s.rstrip()
				s = [j for j in s]
				numbers = []
				while 'Z' in s:
					numbers.append('0')
					s.remove('Z')
					s.remove('E')
					s.remove('R')
					s.remove('O')
				while 'X' in s:
					numbers.append('6')
					s.remove('S')
					s.remove('I')
					s.remove('X')
				while 'G' in s:
					numbers.append('8')
					s.remove('E')
					s.remove('I')
					s.remove('G')
					s.remove('H')
					s.remove('T')
				while 'S' in s and 'V' in s:
					numbers.append('7')
					s.remove('S')
					s.remove('E')
					s.remove('V')
					s.remove('E')
					s.remove('N')
				while 'F' in s and 'V' in s:
					numbers.append('5')
					s.remove('F')
					s.remove('I')
					s.remove('V')
					s.remove('E')
				while 'U' in s:
					numbers.append('4')
					s.remove('F')
					s.remove('O')
					s.remove('U')
					s.remove('R')
				while 'W' in s:
					numbers.append('2')
					s.remove('T')
					s.remove('W')
					s.remove('O')
				while 'H' in s:
					numbers.append('3')
					s.remove('T')
					s.remove('H')
					s.remove('R')
					s.remove('E')
					s.remove('E')
				while 'O' in s:
					numbers.append('1')
					s.remove('O')
					s.remove('N')
					s.remove('E')
				while 'N' in s:
					numbers.append('9')
					s.remove('N')
					s.remove('I')
					s.remove('N')
					s.remove('E')
				#print(s)
				numbers = sorted(numbers)
				#print("Case #{}: {}\n".format(case, "".join(numbers)))
				aout.write("Case #{}: {}\n".format(case, "".join(numbers)))
				case += 1