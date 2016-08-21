'''
Created on 09-Apr-2016

@author: nigel
'''

import time


def find_sequence(k, c, s, f2):
    exp = k**c
    step = exp/s
    i = 1
    while (i <= exp):
        f2.write(" " + str(i))
        i += step
    f2.write("\n")
         

if __name__ == '__main__':
    start = time.time()
    f1 = open('d_small_input.in', 'r')
    f2 = open('d_small_output.in', 'w')
    t = int(f1.readline())
    for i in range(t):
        line = f1.readline().rstrip()
        in_list = line.split(" ")
        k = int(in_list[0])
        c = int(in_list[1])
        s = int(in_list[2])
        f2.write("Case #{}:".format(i + 1))
        find_sequence(k, c, s, f2)
    f1.close()
    f2.close()
    end = time.time()
    print end - start