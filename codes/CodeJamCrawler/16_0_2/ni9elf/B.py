'''
Created on 09-Apr-2016

@author: nigel
'''

import time

def count_moves(pcake):
    moves = 0
    pcake = pcake.rsplit('-', 1)
    if (len(pcake) == 1):
        return moves
    pcake = pcake[0] + '-'
    ch1 = pcake[0]
    i = 1
    while (i < len(pcake)):
        ch2 = pcake[i]
        if(ch1 != ch2):
            moves += 1
            ch1 = ch2
        i += 1
    return (moves+1)


if __name__ == '__main__':
    start = time.time()
    f1 = open('b_large_input.in', 'r')
    f2 = open('b_large_output.in', 'w')
    t = int(f1.readline())
    for i in range(t):
        pcake = f1.readline().rstrip()
        f2.write("Case #{}: {}\n".format(i + 1, count_moves(pcake)))
    f1.close()
    f2.close()
    end = time.time()
    print end - start