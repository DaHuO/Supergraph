import time
import re


def check_required_swaps(pancakes_stack):
    pattern_minus = re.compile("-+")
    pattern_plus = re.compile("\++")
    found_minuses = len(pattern_minus.findall(pancakes_stack))
    found_pluses = len(pattern_plus.findall(pancakes_stack))
    if pancakes_stack.endswith('+'):
        return found_minuses + found_pluses - 1
    return found_minuses + found_pluses


start_time = time.time()

inputFile = open("B-large.in", 'r')
outputFile = open("pancakesOutput.txt", 'w')

number_of_lines = int(inputFile.readline())
print(str(number_of_lines) + ' cases:')

for caseNumber in range(number_of_lines):
    stack = inputFile.readline().rstrip()
    outputFile.write('Case #%d: %s\n' % (caseNumber + 1, check_required_swaps(stack)))

inputFile.close()
outputFile.close()

print("--- %s seconds ---" % (time.time() - start_time))
