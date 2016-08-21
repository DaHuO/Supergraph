__author__ = 'benoitcotte'
# import sys
import math
import random

# Run with the following commands:
# for printing into terminal: python store_credit.py < A-small-practice.in
# for printing into output file: python store_credit.py < A-small-practice.in > A-small-practice.out
# for debugging uncomment following line with path/to/script
# file_name = sys.argv[1]
# fp = open(file_name)
# sys.stdin = fp

INPUT_VARIABLE_NAMES = ["N", "J"]
NUM_OF_CASES = int(raw_input())  # read a line with a single integer

# Combination of numbers for a number of length N with 2 elements: 2^(N-1)
# N=1 => 1 (1)
# N=2 => 2 (10, 11)
# N=3 => 4 (100, 101, 110, 111)
# N=4 => 8 (1000)

def isNotPrime(num, divisor_max):
    for i in range(2, int(divisor_max) + 1):
        if (num % i) == 0:
            return True, i
    else:
        return False, None

class Jamcoin:
    def __init__(self, value, divisors):
        self.value = value
        self.divisors = divisors

    def get_value(self):
        return self.value

    def get_divisors(self):
        return self.divisors

    def __str__(self):
        return "Jamcoin: {} / divisors: {}".format(self.get_value(), self.get_divisors())

class JamcoinFactory:
    history = []

    def __init__(self, N, seed):
        self.N = N
        self.seed = seed

    def create_jamcoin(self):
        """
        Create a jam coin by generating a number until valid for check prime condition
        """
        valid = False
        while not valid:
            # Init divisors and random_number_bit
            divisors = []
            random_number_bit = '0'

            while random_number_bit[-1] is not '1':
                random_number = random.randrange(int("1{}1".format("0" * (self.N - 2)), 2),
                                                 int("1{}1".format("1" * (self.N - 2)), 2))
                random_number_bit = "{0:b}".format(random_number)

            # Check prime condition
            for base in range(2, 11):
                status, divisor = isNotPrime(int(random_number_bit, base), int(random_number_bit, base) ** (1.0/base))
                if status and divisor is not int(random_number_bit, base):
                    valid = True
                    divisors.append(str(divisor))
                else:
                    valid = False
                    break

            if valid:
                return Jamcoin(random_number_bit, divisors)

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

    for i in xrange(1, (NUM_OF_CASES + 1)):
        current_case_number = ((i - 1) / len(INPUT_VARIABLE_NAMES)) + 1

        if not cases_data.get(current_case_number):
            cases_data[current_case_number] = {}

        cases_data[current_case_number]["N"], cases_data[current_case_number]["J"] = (int(s) for s in raw_input().split(" "))

    return cases_data

def compute_data(cases_data):
    """
    Implement logic
    """
    cases_results = []
    for case_number, case_data in cases_data.iteritems():
        case_results = []
        factory = JamcoinFactory(case_data["N"], 1)

        while len(case_results) < case_data["J"]:
            jamcoin = factory.create_jamcoin()
            if jamcoin.get_value() not in factory.history:
                case_results.append([jamcoin.get_value(), jamcoin.get_divisors()])
            factory.history.append(jamcoin.get_value())

        cases_results.append(case_results)

    return cases_results

def print_cases_data(cases_results):
    """
    Print cases data
    """
    for index, case_result in enumerate(cases_results):
        print "Case #{}:".format(index + 1)
        for jamcoin in case_result:
            print "{} {}".format(jamcoin[0], (" ").join(jamcoin[1]))

if __name__ == '__main__':
    cases_data = load_cases_data()
    cases_results = compute_data(cases_data)
    print_cases_data(cases_results)