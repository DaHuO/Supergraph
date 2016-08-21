numbers = [
    "ZERO", # Z
    "ONE",
    "TWO",  # W
    "THREE",
    "FOUR", # R
    "FIVE",
    "SIX",  # X
    "SEVEN", # S
    "EIGHT", # G
    "NINE",
]

uniq_map = [
    ('Z', 0),
    ('W', 2),
    ('X', 6),
    ('S', 7),
    ('G', 8),
    ('H', 3),
    ('R', 4),
    ('O', 1),
    ('F', 5),
    ('N', 9),
]

import copy

def fetch(i, phone_num):
    n = numbers[i]
    cpn = copy.deepcopy(phone_num);
    for c in n:
        #print c, cpn
        if c in cpn:
            del(cpn[cpn.index(c)])
        else:
            return None, phone_num
    return str(i), cpn

def run(items):
    phone_num = [n for n in items[0]]
    #print phone_num

    digit_num = []
    for c, i in uniq_map:
        #print c, i
        while True:
            if c in phone_num:
                digit_num.append(str(i))
                for n in numbers[i]:
                    phone_num.remove(n)
            else:
                break
    if phone_num:
        print "ERROR", phone_num

    return "".join(sorted(digit_num))


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    items = raw_input().split(" ")
    #if i != 28:
    #    continue
    result = run(items)
    print "Case #{}: {}".format(i, result)
    # check out .format's specification for more formatting options
