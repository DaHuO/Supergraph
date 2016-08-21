# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for kk in xrange(1, t + 1):
    alphabet_list = [s for s in raw_input().split(" ")[0]]
    L = len(alphabet_list)
    a_string = 'ZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINE'
    a_list = list(set([s for s in a_string]))
    a_dict = {}
    for elem in a_list:
        a_dict[elem] = 0
    for s in alphabet_list:
        a_dict[s] += 1
    res_list = []
    zero_count = a_dict['Z']
    for i in range(zero_count):
        res_list.append(0)
        a_dict['E'] = a_dict['E'] - 1
        a_dict['R'] = a_dict['R'] - 1
        a_dict['O'] = a_dict['O'] - 1
        a_dict['Z'] = 0
    two_count = a_dict['W']
    for i in range(two_count):
        res_list.append(2)
        a_dict['T'] = a_dict['T'] - 1
        a_dict['O'] = a_dict['O'] - 1
        a_dict['W'] = 0
    four_count = a_dict['U']
    for i in range(four_count):
        res_list.append(4)
        a_dict['F'] = a_dict['F'] - 1
        a_dict['O'] = a_dict['O'] - 1
        a_dict['U'] = 0
        a_dict['R'] = a_dict['R'] - 1
    one_count = a_dict['O']
    #print one_count
    for i in range(one_count):
        #print "in one!"
        res_list.append(1)
        a_dict['N'] = a_dict['N'] - 1
        a_dict['E'] = a_dict['E'] - 1
        a_dict['O'] = 0
    five_count = a_dict['F']
    for i in range(five_count):
        res_list.append(5)
        a_dict['F'] = 0
        a_dict['I'] = a_dict['I'] - 1
        a_dict['V'] = a_dict['V'] - 1
        a_dict['E'] = a_dict['E'] - 1
    six_count = a_dict['X']
    for i in range(six_count):
        res_list.append(6)
        a_dict['S'] = a_dict['S'] - 1
        a_dict['I'] = a_dict['I'] - 1
        a_dict['X'] = 0
    seven_count = a_dict['S']
    for i in range(seven_count):
        res_list.append(7)
        a_dict['S'] = 0
        a_dict['E'] = a_dict['E'] - 2 * 1
        a_dict['V'] = a_dict['V'] - 1
        a_dict['N'] = a_dict['N'] - 1
    eight_count = a_dict['G']
    for i in range(eight_count):
        res_list.append(8)
        a_dict['E'] = a_dict['E'] - 1
        a_dict['I'] = a_dict['I'] - 1
        a_dict['G'] = 0
        a_dict['H'] = a_dict['H'] - 1
        a_dict['T'] = a_dict['T'] - 1
    three_count = a_dict['H']
    for i in range(three_count):
        res_list.append(3)
        a_dict['T'] = a_dict['T'] - 1
        a_dict['H'] = 0
        a_dict['R'] = a_dict['R'] - 1
        a_dict['E'] = a_dict['E'] - 2 * 1
    nine_count = a_dict['I']
    for i in range(nine_count):
        res_list.append(9)
        a_dict['N'] = a_dict['N'] - 2 * 1
        a_dict['I'] = a_dict['I'] - 1
        a_dict['E'] = a_dict['E'] - 1
    sorted_res = sorted(res_list)
    sorted_res_str_l = [str(x) for x in sorted_res]
    res = ''.join(sorted_res_str_l)
        
    print "Case #{}: {}".format(kk, res)
  # check out .format's specification for more formatting options
