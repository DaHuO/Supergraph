import sys

def count_sheeps(line_list):
    """
    """
    number_picked = int(line_list[0])
    numbers_seen = set()
    loop = 0

    if not number_picked:
        return 'INSOMNIA'

    while len(numbers_seen) != 10:
        loop += 1
        numbers = number_picked * loop
        loop_set = set(str(numbers))
        numbers_seen.update(loop_set)

    return numbers

try:
    file_name = sys.argv[1]
except:
    print 5 * 'TEST '
    file_name = 'test.in'

with open(file_name,'r') as input_obj:
    input_obj.next()
    for test,line in enumerate(input_obj,1):
        line_list = line.split()
        result = count_sheeps(line_list)
        print 'Case #{}: {}'.format(test,result)

