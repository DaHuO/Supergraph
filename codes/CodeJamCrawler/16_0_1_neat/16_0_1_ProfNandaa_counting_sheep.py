
# Qualification Round

import sys

def counting_sheep(input, output):

    fo = open(output, 'w')

    line_out = ''

    with open(input, 'r') as f:
        for test_case, line in enumerate(f):
            if test_case > 0: # skip test_case_count
                if int(line) == 0:
                    line_out = 'INSOMNIA'
                else:
                    seen = set()
                    all_seen = False
                    i = 1
                    numbers = line[:-1] # exclude the \n
                    N = int(numbers)

                    while not all_seen:
                        for number in numbers:
                            seen.add(int(number))

                        if sum(seen) == 45 and 0 in seen:
                            line_out = numbers
                            all_seen = True
                        else:
                            i += 1
                            numbers = str(N * i)

                if line_out != '':
                    fo.write('Case #{}: {}\n'.format(test_case, line_out))

    fo.close()


if __name__ == '__main__':
    counting_sheep(sys.argv[1], sys.argv[2])
