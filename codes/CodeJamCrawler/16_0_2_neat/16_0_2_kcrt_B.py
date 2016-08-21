# -*- coding: utf-8 -*-


def check_all_happy(pancake_list):
    for x in pancake_list:
        if(not x):
            return False
    return True

def flip(pancake_list, flip_no):

    pancake_list = pancake_list[:]

    for i in range(flip_no + 1):
        pancake_list[i] = not pancake_list[i]

    if flip_no == len(pancake_list) - 1:
        return list(reversed(pancake_list))
    else:
        return list(reversed(pancake_list[0:flip_no+1])) + list(pancake_list[flip_no+1:])


T = int(input())
for t in range(T):
    S = input()

    bS = [ x == '+' for x in S]
    n_flip = 0

    while not check_all_happy(bS):
        first_different = len(bS)
        for (i, b) in enumerate(bS):
            if b != bS[0]:
                first_different = i
                break
        bS = flip(bS, first_different - 1)

        #print(str(bS))
        n_flip += 1

    result = n_flip
    print("Case #" + str(t + 1) + ": " + str(result))
