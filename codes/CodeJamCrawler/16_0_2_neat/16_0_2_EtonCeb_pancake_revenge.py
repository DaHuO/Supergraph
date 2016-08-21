__author__ = 'benoitcotte'
# import sys

# Run with the following commands:
# for printing into terminal: python store_credit.py < A-small-practice.in
# for printing into output file: python store_credit.py < A-small-practice.in > A-small-practice.out
# for debugging uncomment following line with path/to/script
# file_name = sys.argv[1]
# fp = open(file_name)
# sys.stdin = fp

INPUT_VARIABLE_NAMES = ["S"]
NUM_OF_CASES = int(raw_input())  # read a line with a single integer

def load_cases_data():
    """
    Load cases data into a dict of structure:
    {
        <case_number>: {
            <input_var_name>: <list of values>
        }
    }
    For a stack of pancakes: list of values is a list
    with FIRST item being at the BOTTOM and LAST at the TOP
    """
    cases_data = {}

    for i in xrange(1, (NUM_OF_CASES * len(INPUT_VARIABLE_NAMES)) + 1):
        current_case_number = ((i - 1) / len(INPUT_VARIABLE_NAMES)) + 1

        if not cases_data.get(current_case_number):
            cases_data[current_case_number] = {}

        cases_data[current_case_number][INPUT_VARIABLE_NAMES[(i - 1) % len(INPUT_VARIABLE_NAMES)]] = \
             map(lambda x: True if x == '+' else False, raw_input())[::-1]  # read a list of integers

    return cases_data

def sort_pancakes(stack, maneuver_number):
    # Given a stack, sort the stack and increment maneuver number
    i = len(stack) - 1
    while i > 0:
        # If pancake is face up
        if stack[i] == stack[i - 1]:
            # Then pass to next pancake
            i -= 1
            continue

        # Otherwise flip all next pancakes
        # is False
        else:
            stack[i:] = map(lambda x: not x, stack[i:])[::-1]
            maneuver_number += 1
        i -= 1

    # Base case if all array is false
    if not stack[0]:
        stack[i:] = map(lambda x: not x, stack[i:])[::-1]
        maneuver_number += 1

    return stack, maneuver_number



def compute_data(cases_data):
    """
    Implement logic
    """
    cases_results = []
    for case_number, case_data in cases_data.iteritems():
        maneuver_number = 0
        pancake_stack = case_data["S"]

        # For a pancake in the stack starting from bottom
        sorted_stack, maneuver_number,  = sort_pancakes(pancake_stack, maneuver_number)

        cases_results.append(maneuver_number)

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