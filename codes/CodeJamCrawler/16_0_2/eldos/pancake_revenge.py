from copy import deepcopy

def abs_max_pos(_list):
    abs_max = 0
    pos = 0
    for i in range(len(_list)):
        if abs(_list[i]) > abs_max:
            abs_max = abs(_list[i])
            pos = i
        # elif abs(_list[i]) == abs_max:
        #     if _list[i] > _list[pos]:
        #         pos = i
    return pos

def first_invert(_list):
    for i in range(1, len(_list)):
        if _list[i-1] * _list[i] == -1:
            return i

cases = int(input())
for i in range(cases):
    flips = 0
    cakes = map(lambda x: 1 if x is '+' else -1, list(raw_input()))
    total = sum(cakes)
    length = len(cakes)
    while total != length:
        # print cakes
        sum_list = deepcopy(cakes)
        for j in range(1, len(sum_list)):
            sum_list[j] += sum_list[j-1]
        max_list = map(lambda x: -2*x + total, sum_list)
        flip = abs_max_pos(max_list) + 1
        if abs(max_list[flip-1]) <= total:
            flip = first_invert(cakes)
        cakes[0:flip] = map(lambda x: -x, cakes[0:flip])
        total = sum(cakes)
        flips += 1
    print("Case #%d: %d" % (i+1, flips))