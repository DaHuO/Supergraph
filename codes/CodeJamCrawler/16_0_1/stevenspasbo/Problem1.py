import sys

# file_name = "A-small-attempt0.in"
file_name = sys.argv[1]

the_file = open(file_name, 'r')


def get_number(i):
    return int(i)


def get_last_digit(i):
    return i % 10


def has_all_digits(the_hash):
    for i in range(0, 10):
        if i not in the_hash:
            return False
    return True


def count_sheep(n, step=1, dict={}):
    if n == 0:
        return "INSOMNIA"
    i = n * step
    while i > 0:
        curr_digit = get_last_digit(i)
        if curr_digit not in dict:
            dict[curr_digit] = 1
        if has_all_digits(dict):
            return n * step
        i = i / 10
    return count_sheep(n, step + 1, dict)


first_line = True
case_num = 1
for row in the_file:
    num = int(row)
    if not first_line:
        print "Case #%d: %s" % (case_num, str(count_sheep(num, 1, {})))
        case_num = case_num + 1
    first_line = False


# Set step to 1
# Create empty dictionary
# Read line
# Split line into character array
# Read each character, inserting into dictionary as key
# Check that dictionary has 0-9
# If so: return current line
# Else increment step and multiply current line and check again
