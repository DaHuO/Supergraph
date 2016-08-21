'''
Created on Apr 9, 2016

@author: nguyen
'''

import sys

def first_factor(n):
    if n % 2 == 0:
        return 2
    i = 3
    sqn = int(n ** 0.5)
    while i <= sqn:
        if n % i == 0:
            return i
        i += 1
    return 1

def str_to_int(instr, base):
    result = 0
    instr = instr[::-1]
    for i in range(len(instr)):
        result += int(instr[i]) * (base ** i)
    return result

if __name__ == '__main__':
    if len(sys.argv) < 2:
        pass

    with open(sys.argv[1], 'r') as fi:
        with open('coin_jam_output.txt', 'w') as fo:
            count = int(fi.readline())
            for i in range(count):
                fo.write('Case #%d:\n' % (i+1))
                instrs = fi.readline().strip().split()
                N = int(instrs[0])
                J = int(instrs[1])
                print str(N) + ' ' + str(J) + '\n'

                if N % 2 == 0:
                    max_pos = (N - 2) / 2
                    pos = [(x, y, z, t)
                                for x in range(max_pos) for y in range(max_pos)
                                for z in range(max_pos) for t in range(max_pos)
                                if x > y and z > t]
                    j = 0
                    while j < J:
                        inner_str = ['0'] * (N - 2)
                        inner_str[2 * pos[j][0]] = inner_str[2 * pos[j][1]] \
                        = inner_str[2 * pos[j][2] + 1] \
                        = inner_str[2 * pos[j][3] + 1] \
                        = '1'
                        coin = '1' + ''.join(inner_str) + '1'
                        base6 = str_to_int(coin, 6)
                        factor6 = first_factor(base6)
                        if factor6 > 1:
                            fo.write(coin + ' 3 2 3 2 ' + str(factor6) + ' 2 3 2 3\n')
                            j += 1
                else:
                    max_odd_pos = (N - 2) / 2
                    max_even_pos = N - 2 - max_odd_pos
                    pos = [(x, y, z, t)
                            for x in range(max_even_pos) for y in range(max_odd_pos)
                            for z in range(max_odd_pos) for t in range(max_odd_pos)
                            if y > z and z > t]
                    j = 0
                    while j < J:
                        inner_str = ['0'] * (N - 2)
                        inner_str[2 * pos[j][0] + 1] = inner_str[2 * pos[j][1]] \
                        = inner_str[2 * pos[j][2]] \
                        = inner_str[2 * pos[j][3]] \
                        = '1'
                        inner_str = inner_str[::-1]
                        coin = '1' + ''.join(inner_str) + '1'
                        base6 = str_to_int(coin, 6)
                        factor6 = first_factor(base6)
                        if factor6 > 1:
                            fo.write(coin + ' 3 2 3 2 ' + str(factor6) + ' 2 3 2 3\n')
                            j += 1
    pass