q = []
with open('A-large.in', 'rb') as f:
    count = 0
    for i in f:
        if count == 0:
            count = 1
            continue
        i = int(i.strip().decode("utf-8"))
        q.append(i)


def convert_to_digits(num):
    s  = str(num)
    n_list = [int(d) for d in s]
    return set(n_list)


def is_magic_number(no, case):
    values_so_far = set([0,1,2,3,4,5,6,7,8,9])
    my_set = set()
    c = 0
    if no == 0:
        print("Case #{}: ".format(case) + "INSOMNIA")
        return
    while values_so_far != my_set:
        c += 1
        n = no * c
        my_set = my_set.union(convert_to_digits(n))
    print("Case #{}: ".format(case) + str(n))

for a, val in enumerate(q):
    is_magic_number(val, a+1)
