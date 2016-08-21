from sys import argv

IN_FILE = argv[1]
OUT_FILE = 'out.txt'

num_tests = 0
seeds = []
last_nums = []
ALL_DIGITS = set('0123456789')

def get_last_num (seed, i, digit_set):
    num_to_str = str(seed * i)
    for c in num_to_str:
        digit_set.add(c)
    if not ALL_DIGITS - digit_set:
        return num_to_str
    else:
        return get_last_num(seed, i + 1, digit_set)

with open (IN_FILE, 'r') as r:
    for i, line in enumerate(r):
        if not i:
            num_tests = int(line.rstrip())
        else:
            seeds.append(int(line.rstrip()))


for i in xrange(num_tests):
    try:
        last_nums.append(get_last_num(seeds[i], 1, set()))
    except:
        last_nums.append('INSOMNIA')

with open (OUT_FILE, 'w') as w:
    for i, last_num in enumerate(last_nums):
        w.write('Case #' + str(i + 1) + ': ' + last_num + '\n')
