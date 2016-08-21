import itertools

def main():
	f = open('A-small-attempt0.in', 'r')
	fout = open('output_{}'.format(f.name), 'w')

	numberTestCase = int(f.readline())


	for i in range(1, numberTestCase + 1):
		w = list(f.readline().strip('\n'))

		d = dict()
		after = list()
		before = list()
		length = 1
		start = True

		d[1] = w.pop(0)

		while len(w) > 0:
			charac = w.pop(0)

			after = list()
			before = list()

			after.extend(d[length])
			before.extend(d[length])

			after = [charac + i for i in after]
			before = [i + charac for i in before]

			length += 1
			d[length] = after
			d[length].extend(before)

		#print("".join(l))
		#print(d)
		finalList = list(d[length])
		finalList.sort()
		#print()


		fout.write('Case #{}: {}\n'.format(i, finalList.pop()))


if __name__ == "__main__":
    main()
