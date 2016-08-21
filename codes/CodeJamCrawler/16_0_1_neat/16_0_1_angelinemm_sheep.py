INSOMNIA = "INSOMNIA"

def maybe_add(_list, item):
    if item not in _list:
        _list.append(item)
    return _list

def get_digits(string_number):
    digits = []
    for number in string_number:
        digits = maybe_add(digits, int(number))
    return digits

def last_number(N):
    if N == "0":
        return INSOMNIA
    seen_numbers = []
    i = 1
    num_N = int(N)
    while len(seen_numbers) < 10:
        N = str(i * num_N)
        for digit in get_digits(N):
            seen_numbers = maybe_add(seen_numbers, digit)
        i += 1
    return N

f_in = open('input.txt', 'r')
f_out = open('output.txt', 'w')

nb_tests = int(f_in.readline())
for i in range (1, nb_tests+1):
    N = f_in.readline().rstrip('\n')
    result = last_number(N)
    f_out.write('Case #{}: {}'. format(i, result))
    f_out.write('\n')
