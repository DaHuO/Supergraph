import sys
import utils

fname = sys.argv[1]

def get_ans(case):
    pancakes = case[0]
    flips = 0

    while pancakes and pancakes[-1]:
        pancakes = pancakes[:-1]

    pos_c = pancakes.count(True)
    neg_c = pancakes.count(False)
    major_class = True

    if pos_c < neg_c:
        flips += 1
        major_class = False

    def flip(arr, k):
        for i in range((k / 2) + 1):
            arr[i], arr[k-i] = not arr[k-i], not arr[i]

    while pancakes:
        if pancakes[-1] != major_class:
            if pancakes[0] == major_class:
                fpoint = pancakes.index(not major_class) - 1
                flip(pancakes, fpoint)
                flips += 1

            flip(pancakes, len(pancakes) - 1)
            flips += 1

        pancakes = pancakes[:-1]

    return flips

def map_to_bool(x):
    if x == '+':
        return True
    return False

utils.process(fname, 1, [ lambda x: map(map_to_bool, list(x)) ], get_ans)
