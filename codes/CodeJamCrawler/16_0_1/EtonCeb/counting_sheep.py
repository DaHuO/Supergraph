__author__ = 'benoitcotte'
# import sys

# Run with the following commands:
# for printing into terminal: python store_credit.py < A-small-practice.in
# for printing into output file: python store_credit.py < A-small-practice.in > A-small-practice.out
# for debugging uncomment following line with path/to/script
# file_name = sys.argv[1]
# fp = open(file_name)
# sys.stdin = fp

INPUT_VARIABLE_NAMES = ["N"]
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

def compute_data(cases_data):
    """
    Implement logic
    """
    cases_results = []

    for case_number, case_data in cases_data.iteritems():
        case_results = []
        n_set = set()
        multiplicator = 0

        while len(n_set) < 10:

            multiplicator += 1
            digits = map(lambda x: int(x), str(multiplicator * case_data['N'][0]))
            n_set.update(digits)

            # Break condition
            if multiplicator > case_data['N'][0] * multiplicator:
                case_results.append("INSOMNIA")
                break

        if case_results:
            cases_results.append(case_results[0])
        else:
            cases_results.append(multiplicator * case_data['N'][0])

    return cases_results

def print_cases_data(cases_results):
    """
    Print cases data
    """
    for index, case_result in enumerate(cases_results):
        print "Case #{}: {}".format(index + 1, cases_results[index])

if __name__ == '__main__':
    cases_data = load_cases_data()
    cases_results = compute_data(cases_data)
    print_cases_data(cases_results)

# Complementary information
# Pareto distribution: The proportion of {X} with at least {m} digits (before the decimal point),
# where {m} is above the median number of digits, should obey an approximate exponential law,
# i.e. be approximately of the form {c 10^{-m/\alpha}} for some {c, \alpha > 0}.
# Again, in many cases {\alpha} is close to {1}.
# source: https://terrytao.wordpress.com/2009/07/03/benfords-law-zipfs-law-and-the-pareto-distribution/
