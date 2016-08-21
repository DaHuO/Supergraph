import os
script_path = os.path.dirname(__file__)


def last_number(N):
    """ Finds the last number she fall asleep for a given number
    Args:
        N: Any number between limits
    """
    last_number = 'INSOMNIA'
    if N == 0 or N < 0 or N > 1000000:  # if we are out of limits return insomnia
        return last_number
    tracked = []  # track digits in a list
    i = 1
    while len(tracked) < 10:
        N_string = str(i * N)  # convert number into a string
        for n in N_string:
            # check track list and add n if it is not in the track list
            tracked.append(int(n)) if int(n) not in tracked else True
        last_number = i * N
        i += 1
    return last_number

# read input file line by line
with open(os.path.join(script_path, 'A-large.in')) as f:
    input = [x.strip('\n') for x in f.readlines()]

# create desired output
output = ''
case_no = 1
for l in range(1, len(input), 1):
    N = int(input[l])
    result = str(last_number(N))
    output += 'Case #' + str(case_no) + ':' + ' ' + result + '\n'
    case_no += 1
    if case_no == 101:
        break

f = open(os.path.join(script_path, 'output.txt'), 'w')
f.write(output)
f.close()
