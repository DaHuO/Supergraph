# Google Code Jam Qualification Round 2016
# Problem B. Revenge of the Pancakes
# Author: Nodari Lipartiya <nodari.lipartiya@gmail.com>


def fn(cakes):
    """ can't choose good name now
    """
    happy_count = 0
    uphappy_count = 0
    switch_count = 0
    prev_item = None

    for item in cakes:
        if item != prev_item and prev_item:
            switch_count += 1

            if switch_count > 1:
                return

        if item == '+':
            happy_count += 1
        else:
            uphappy_count += 1

        prev_item = item

    if happy_count + uphappy_count == len(cakes):
        return True


def make_maneuver(cakes):
    cakes.reverse()
    for i in xrange(len(cakes)):
        if cakes[i] == '+':
            cakes[i] = '-'
        else:
            cakes[i] = '+'
    return cakes


def process_random(cakes):
    maneuvers = 0
    cake_count = 0
    prev_cake = None
    
    for i in xrange(len(cakes)):
        if not prev_cake:
            prev_cake = cakes[i]
            continue

        if fn(cakes):
            if cakes[0] == '-':
                maneuvers += 1
            else:
                maneuvers += 2

            break

        if prev_cake != cakes[i]:
            cakes = make_maneuver(cakes[:i]) + cakes[i:]
            maneuvers += 1
        
        prev_cake = cakes[i]

    return maneuvers


def process_cakes(cakes):
    cakes_len = len(cakes)

    if len(filter(lambda x: x == '+', cakes)) == cakes_len:
        return 0

    if len(filter(lambda x: x == '-', cakes)) == cakes_len:
        return 1

    # if stack looks like ++++---- or ----++++
    # we need exactly to moves
    if fn(cakes):
        if cakes[0] == '-':
            return 1
        else:
            return 2

    return process_random(cakes)


line_number = 1
num_of_test_cases = 0

with open('B-large.in') as input_file, open('_b_output_large.out', 'w+') as output_file:
    for line in input_file.readlines():
        if line_number == 1:
            num_of_test_cases = int(line)
            line_number += 1
            continue

        case = list(line.strip('\n'))
        case_num = line_number - 1
        if num_of_test_cases == case_num:
            output_file.write('Case #{}: {}'.format(case_num, process_cakes(case)))
        else:
            output_file.write('Case #{}: {}\n'.format(case_num, process_cakes(case)))
        line_number += 1