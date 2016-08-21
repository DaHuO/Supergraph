#!/usr/bin/env python

###
# Input here
###
input = []
total = -1
with open('./input.txt') as f:
    input = f.readlines()
    total = int(input.pop(0))

###
# "Work work work" - Rihanna
###

def parse_numbers(number):
    values = {}
    incoming_number = str(number)
    for i in incoming_number:
        current = int(i)
        values[current] = True
    return values

result = []

def check_success(tallies):
    success = True
    counter = 0
    for i in tallies:
        counter += 1
        if tallies[i] is False:
            success = False

    return success

for case_number in range(0, total):
    my_tally = {
      0: False,
      1: False,
      2: False,
      3: False,
      4: False,
      5: False,
      6: False,
      7: False,
      8: False,
      9: False
    }
    starting_n = int(input[case_number])
    should_stop_now = False

    current = starting_n
    for iteration in range(1, 200):
        current = iteration * starting_n

        incoming_update = parse_numbers(current)
        my_tally.update(incoming_update)

        should_stop_now = check_success(my_tally)
        if should_stop_now:
            break

    if should_stop_now == True:
        result.append(current)
    else:
        result.append('INSOMNIA')


###
# Output here
###
write_out = open('./output.txt', 'w')
counter = 0
for item in result:
    counter += 1
    line = str(item)
    write_out.write('Case #')
    write_out.write(str(counter))
    write_out.write(': ')
    write_out.write(line)
    write_out.write('\n')
write_out.close()
