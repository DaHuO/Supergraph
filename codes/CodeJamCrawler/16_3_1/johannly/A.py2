import sys


def get_evacuation_sequence(p, total_p):
	evacuation_sequence = []

	while (not all((x == 0) for x in p)):
		step = []
		new_p = p[:]
		new_total_p = total_p

		max_index = p.index(max(p))

		step += [max_index]
		new_p[max_index] -= 1
		new_total_p -= 1

		for potential_new_violator_index in range(len(p)):
			if (float(new_p[potential_new_violator_index]) / float(new_total_p) > 0.5):
				step += [potential_new_violator_index]
				new_p[potential_new_violator_index] -= 1
				new_total_p -= 1
				break

		evacuation_sequence += [step]

		p = new_p[:]
		total_p = new_total_p

	return evacuation_sequence


input = open(sys.argv[1], 'r')

test_cases = input.readline()
test_cases = int(test_cases)

for test_case in range(test_cases):
	n = input.readline()
	n = int(n)

	p = input.readline()
	p = p.split()
	p = map(int, p)

	evacuation_sequence = get_evacuation_sequence(p, sum(p))
	evacuation_sequence = [[chr(ord('A') + x) for x in step] for step in evacuation_sequence]
	evacuation_sequence = [''.join(step) for step in evacuation_sequence]
	evacuation_sequence = ' '.join(evacuation_sequence)

	print('Case #' + str(test_case + 1) + ': ' + evacuation_sequence)


input.close()
