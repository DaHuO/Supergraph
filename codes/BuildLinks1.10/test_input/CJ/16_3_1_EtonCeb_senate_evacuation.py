__author__ = 'benoitcotte'
import sys

# Run with the following commands:
# for printing into terminal: python store_credit.py < A-small-practice.in
# for printing into output file: python store_credit.py < A-small-practice.in > A-small-practice.out
# for debugging uncomment following line with path/to/script
# file_name = sys.argv[1]
# fp = open(file_name)
# sys.stdin = fp

INPUT_VARIABLE_NAMES = ["N", "P"]
NUM_OF_CASES = int(raw_input())  # read a line with a single integer

def load_cases_data():
	"""
	Load cases data into a dict of structure:
	{
		<case_number>: {
			<input_var_name>: <list of values>
		}
	}

	"""
	cases_data = {}

	for i in xrange(1, (NUM_OF_CASES * len(INPUT_VARIABLE_NAMES)) + 1):
		current_case_number = ((i - 1) / len(INPUT_VARIABLE_NAMES)) + 1

		if not cases_data.get(current_case_number):
			cases_data[current_case_number] = {}

		cases_data[current_case_number][INPUT_VARIABLE_NAMES[(i - 1) % len(INPUT_VARIABLE_NAMES)]] = \
			[int(s) for s in raw_input().split(" ")]  # read a list of integers

	return cases_data

def noAbsoluteMajority(name, parties_pop, number_to_remove):
	total = sum(parties_pop)
	party_distributions = []
	for party_name, pop in enumerate(parties_pop):
		if party_name == name:
			party_distributions.append(float(pop - number_to_remove) / float(total - number_to_remove))
		else:
			party_distributions.append(float(pop) / float(total - number_to_remove))

	return all([party_distribution <= 0.5 for party_distribution in party_distributions])

def compute_data(cases_data):
	cases_results = []

	for k, case_data in cases_data.iteritems():

		case_results = []
		P = case_data['P']

		while any(P):
			for i, pop in enumerate(P):

				if pop >= 2 and noAbsoluteMajority(i, P, 2):
					P[i] -= 2
					case_results.append('{}{}'.format(chr(ord('A') + i), chr(ord('A') + i)))

				elif pop >= 1 and noAbsoluteMajority(i, P, 1):
					P[i] -= 1
					case_results.append('{}'.format(chr(ord('A') + i)))

				# Case of two parties are draw
				elif len([population for population in P if population > 0]) == 2:
					temp = []
					for j, p in enumerate(P):
						if p is not 0:
							P[j] -= 1
							temp.append(j)
					case_results.append('{}{}'.format(chr(ord('A') + temp[0]), chr(ord('A') + temp[1])))
		cases_results.append(case_results)
	return cases_results



def print_cases_data(cases_results):
	"""
	Print cases data
	"""
	for index, case_result in enumerate(cases_results):
		print "Case #{}: {}".format(index + 1, " ".join(case_result))

if __name__ == '__main__':
	cases_data = load_cases_data()
	cases_results = compute_data(cases_data)
	print_cases_data(cases_results)