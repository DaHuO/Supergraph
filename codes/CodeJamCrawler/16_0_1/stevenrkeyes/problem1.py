def get_digits(number):
    if number < 0:
        return get_digits(-number)
    else:
        return [int(i) for i in str(number)]

def is_all_digits(some_set):
    return all([i in some_set for i in range(10)])

def get_sleep_number(N):
    if N == 0:
        return "INSOMNIA"
    i = 0
    digits_named = set()
    while not is_all_digits(digits_named):
        i += 1
        digits_named.update(get_digits(i*N))
    return i*N

import sys
filename = sys.argv[1]
f = open(filename)
lines = f.readlines()

i = 1
for line in lines[1:]:
    print "Case #" + str(i) + ": " + str(get_sleep_number(int(line)))
    i += 1
