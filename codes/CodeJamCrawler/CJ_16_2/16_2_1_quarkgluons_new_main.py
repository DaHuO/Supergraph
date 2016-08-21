
T = int (raw_input())

for i in range(T):
    print 'Case #%d:' %(i+1),
    s = raw_input()
    s_list = [ch for ch in s]
    res = ''
    for j in range(5):
        if j == 0:
            zeroes = s.count('Z')
            for k in range(zeroes):
                s_list.remove('Z')
                s_list.remove('E')
                s_list.remove('R')
                s_list.remove('O')
                res += '0'
            twos = s.count('W')
            for k in range(twos):
                s_list.remove('T')
                s_list.remove('W')
                s_list.remove('O')
                res += '2'
            sixes = s.count('X')
            for k in range(sixes):
                s_list.remove('S')
                s_list.remove('I')
                s_list.remove('X')
                res += '6'
            eights = s.count('G')
            for k in range(eights):
                s_list.remove('E')
                s_list.remove('I')
                s_list.remove('G')
                s_list.remove('H')
                s_list.remove('T')
                res += '8'
        if j == 1:
            threes = s_list.count('H')
            for k in range(threes):
                s_list.remove('T')
                s_list.remove('H')
                s_list.remove('R')
                s_list.remove('E')
                s_list.remove('E')
                res += '3'
        if j == 2:
            fours = s_list.count('R')
            for k in range(fours):
                s_list.remove('F')
                s_list.remove('O')
                s_list.remove('U')
                s_list.remove('R')
                res += '4'
            sevens = s_list.count('S')
            for k in range(sevens):
                s_list.remove('S')
                s_list.remove('E')
                s_list.remove('V')
                s_list.remove('E')
                s_list.remove('N')
                res += '7'
        if j == 3:
            fives = s_list.count('F')
            for k in range(fives):
                s_list.remove('F')
                s_list.remove('I')
                s_list.remove('V')
                s_list.remove('E')
                res += '5'
        if j == 4:
            nines = s_list.count('I')
            for k in range(nines):
                s_list.remove('N')
                s_list.remove('I')
                s_list.remove('N')
                s_list.remove('E')
                res += '9'
            ones = s_list.count('E')
            for k in range(ones):
                s_list.remove('O')
                s_list.remove('N')
                s_list.remove('E')
                res += '1'
    print ''.join(sorted(res))
