import sys

# Trim any continuous stack of +'s at the bottom of pancake_string
def trim(pancake_string):
    above_plus_stack = pancake_string.rfind('-')
    if above_plus_stack > -1:
        return pancake_string[:above_plus_stack+1]
    else: # No -'s
        return ''

# Return the minimum number of flips needed to get all happy faces up
# (Answer: 1 more than the number of direction switches in the stack)
def min_flips(pancake_string):
    # Trim off any +'s at bottom
    pancake_string = trim(pancake_string)

    # Handle edge case
    if len(pancake_string) == 0:
        return 0

    # Now pancake_string has form X^i- (X is either + or -)
    num_switches = 0
    current_pancake = pancake_string[0]
    for i in xrange(1, len(pancake_string)):
        next_pancake = pancake_string[i]
        if next_pancake != current_pancake:
            num_switches += 1
        current_pancake = next_pancake

    return num_switches + 1

input_lines = sys.stdin.readlines()
num_cases = int(input_lines[0])

for i in xrange(1, num_cases+1):
    pancake_string = input_lines[i].strip()
    answer = min_flips(pancake_string)
    print "Case #%d: %d" % (i, answer)
