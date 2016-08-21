import sys

input_lines = sys.stdin.read().split('\n')

def get_nth_party_name(n):
    return chr(ord('a') + n).capitalize()

def remove(num_senators, nth):
    num_senators[nth] = num_senators[nth] - 1

def get_max_index(num_senators):
    return num_senators.index(max(num_senators))

def has_one_party_only(num_senators):
    count = sum(1 for i in num_senators if i > 0 )
    return count == 1

def has_one_party_majority(num_senators):
    max_sen = max(num_senators)
    count = sum(1 for i in num_senators if i >= max_sen )
    return count == 1

def solve(num_senators):
    result = []
    max_index = get_max_index(num_senators)
    while num_senators[max_index] > 0:
        # print('max_index: {max_index}'.format(max_index=max_index))
        # print('num_senators: {num_senators}'.format(num_senators=num_senators))
        result.append(get_nth_party_name(max_index))
        remove(num_senators, max_index)
        max_index = get_max_index(num_senators)
        if has_one_party_only(num_senators):
            remove(num_senators, max_index)
            result[-1] = result[-1] + get_nth_party_name(max_index)
            max_index = get_max_index(num_senators)
        else:
            remove(num_senators, max_index)
            if not has_one_party_majority(num_senators):
                result[-1] = result[-1] + get_nth_party_name(max_index)
                max_index = get_max_index(num_senators)
            else:
                num_senators[max_index] = num_senators[max_index] + 1
    return ' '.join(result)

def translate_to_array(input_line):
    array = input_line.split(' ')
    return list(map(int, array))

for i in range(1, len(input_lines)):
    if (i % 2) == 1:
        continue
    input_line = input_lines[i]
    if len(input_line) == 0:
        continue
    num_senators = translate_to_array(input_line)
    print("Case #{i}: {result}".format(
        i=i/2, result=solve(num_senators)
    ))
