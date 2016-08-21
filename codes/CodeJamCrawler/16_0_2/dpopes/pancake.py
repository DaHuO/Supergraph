import sys
import time

flip_count = 0

def make_happy(array):
    global flip_count
    #print( "array is {0}".format(array))
    if is_happy(array):
        print(flip_count)
        return
    if is_sad(array):
        print(flip_count + 1)
        return
    if len(array) == 1:
        if is_happy(array):
            print("0")
            return
        else:
            print("1")

    i = 1
    last_seen = array[0]
    for c in array[1:]:
        #print( "i == {0}; last_seen == {1}; c == {2};".format(i, last_seen, c))
        if is_happy(array):
            print(str(flip_count))
            return
        elif c == last_seen:
            last_seen = c
            i+= 1
            continue
        else:
            flipped_part = flip_array(array[0:i])
            #print( "flipped: {0}".format(flipped_part))
            flipped_plus_rest = flipped_part + array[i:]
            #print( "flipped_plus_rest: {0}".format(flipped_plus_rest))
            if is_happy(flipped_plus_rest):
                print(str(flip_count))
                return
            return make_happy(flipped_plus_rest)


def flip_array(array):
    #print( "flipping {0}".format(array))
    global flip_count
    flip_count += 1
    reversed = array[:]
    reversed.reverse()
    return [ '+' if i == '-' else '-' for i in reversed]


def is_happy(array):
    return not sum(1 for c in array if c == '-')


def is_sad(array):
    return not sum(1 for c in array if c == '+')


if __name__ == "__main__":
    T = int(raw_input())
    for i in xrange(1, T + 1):
        pancakes_array = [c for c in raw_input()]
        sys.stdout.write("Case #{0}: ".format(i))
        flip_count = 0
        make_happy(pancakes_array)
