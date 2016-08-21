from collections import Counter, OrderedDict

POSSIBILITIES = OrderedDict()
POSSIBILITIES['ZERO'] = '0'
POSSIBILITIES['ONE'] = '1'
POSSIBILITIES['TWO'] = '2'
POSSIBILITIES['THREE'] = '3'
POSSIBILITIES['FOUR'] = '4'
POSSIBILITIES['FIVE'] = '5'
POSSIBILITIES['SIX'] = '6'
POSSIBILITIES['SEVEN'] = '7'
POSSIBILITIES['EIGHT'] = '8'
POSSIBILITIES['NINE'] = '9'

def can_create(str_number, cnter):
    temp_counter = Counter(cnter)
    temp_counter.subtract(Counter(str_number))

    return all(count >= 0 for count in temp_counter.values())

def recur_create(count, current_number):
    current_count = Counter(count)

    for str_number in POSSIBILITIES.keys():
        if can_create(str_number, current_count):
            temp_counter = Counter(current_count)
            temp_counter.subtract(Counter(str_number))
            temp_current_number = current_number + POSSIBILITIES[str_number]

            if all(count == 0 for count in temp_counter.values()):
                return temp_current_number

            next_recurr = recur_create(temp_counter, current_number)

            if next_recurr is not None:
                current_count.subtract(Counter(str_number))
                current_number = current_number + POSSIBILITIES[str_number]

                return recur_create(current_count, current_number)

number_of_lines = int(raw_input())

for line in range(1, number_of_lines + 1):
    string = str(raw_input())

    cnter = Counter(string)
    result = recur_create(cnter, '')
    result = ''.join(sorted(result))

    print 'Case #{}: {}'.format(line, result)
