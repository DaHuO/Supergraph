__author__ = 'sushrutrathi'

from collections import namedtuple

make_pair = namedtuple("make_pair", ["first", "second"])


with open('input.txt') as f:
    t = int(f.readline().split()[0])
    for case in range(1,t+1):
        g = open('output.txt','a')
        g.write('Case #' + str(case) + ':')
        n = int(f.readline().split()[0])
        arr = [int(a) for a in f.readline().split(' ')]
        new_arr = []
        left = 0
        for i, val in enumerate(arr):
            new_arr.append([val,i])
            left += val

        new_arr = sorted(new_arr, reverse = True)

        while(True):
            g.write(' ' + chr(ord('A') + new_arr[0][1]))
            new_arr[0][0] -= 1
            left -= 1
            if(new_arr[1][0]*2 > left):
                left -= 1
                new_arr[1][0] -=1
                g.write(chr(ord('A') + new_arr[1][1]))


            new_arr = sorted(new_arr, reverse = True)

            if new_arr[0][0]==0:
                break

        g.write('\n')
