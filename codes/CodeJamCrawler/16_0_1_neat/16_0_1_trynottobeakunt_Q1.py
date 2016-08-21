import copy, datetime

SINGLE_INT_ARRAY = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def last_number(org_n):
    if org_n == 0:
        n = "INSOMNIA"
    else:
        single_ints = copy.copy(SINGLE_INT_ARRAY)
        n = 0
        while len(single_ints) > 0:
            n += org_n
            for single_int in str(n):
                if int(single_int) in single_ints:
                    single_ints.remove(int(single_int))
    return n


t_array = []
out_file = open('output.out', 'w')
with open('A-large.in', 'r') as in_file:
    for line in in_file:
        t_array.append(int(line))
        if len(t_array) > 1:
            output = last_number(int(line))
            out_file.write("Case #{0}: {1}\n".format(len(t_array) - 1, output))
out_file.close()
