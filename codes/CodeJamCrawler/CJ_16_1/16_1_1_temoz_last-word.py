def main():
	fname = input()
	with open(fname) as f:
		with open('last-word-large-out.txt', 'w') as w:
			lines = [l.strip() for l in f.readlines()]
			case = 1
			for line in lines[1:]:
				head = line[0]
				tail = line[0]
				last = line[0]
				for char in line[1:]:
					if char >= head:
						last = char + last
						head = char
					else:
						last = last + char
						tail = char
				w.write('Case #%i: %s\n' % (case, last))
				case = case + 1

main()