# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    # read a list of integers, 2 in this case
    n = raw_input().split(" ")[0]
    alpha_dict = {
        'E': 0,
        'F': 0,
        'G': 0,
        'H': 0,
        'I': 0,
        'N': 0,
        'O': 0,
        'R': 0,
        'S': 0,
        'T': 0,
        'U': 0,
        'V': 0,
        'W': 0,
        'X': 0,
        'Z': 0
    }
    for j in range(len(n)):
        for key in alpha_dict:
            if n[j] == key:
                alpha_dict[key] += 1
                break

    num_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # print(alpha_dict)

    # 6
    num_sum[6] = alpha_dict['X']
    alpha_dict['S'] -= num_sum[6]
    alpha_dict['I'] -= num_sum[6]

    # 0
    num_sum[0] = alpha_dict['Z']
    alpha_dict['E'] -= num_sum[0]
    alpha_dict['R'] -= num_sum[0]
    alpha_dict['O'] -= num_sum[0]

    # 2
    num_sum[2] = alpha_dict['W']
    alpha_dict['T'] -= num_sum[2]
    alpha_dict['O'] -= num_sum[2]

    # 4
    num_sum[4] = alpha_dict['U']
    alpha_dict['F'] -= num_sum[4]
    alpha_dict['O'] -= num_sum[4]
    alpha_dict['R'] -= num_sum[4]

    # 5
    num_sum[5] = alpha_dict['F']
    alpha_dict['I'] -= num_sum[5]
    alpha_dict['V'] -= num_sum[5]
    alpha_dict['E'] -= num_sum[5]

    # 8
    num_sum[8] = alpha_dict['G']
    alpha_dict['I'] -= num_sum[8]
    alpha_dict['H'] -= num_sum[8]
    alpha_dict['E'] -= num_sum[8]
    alpha_dict['T'] -= num_sum[8]

    # 1
    num_sum[1] = alpha_dict['O']
    alpha_dict['N'] -= num_sum[1]
    alpha_dict['E'] -= num_sum[1]

    # 3
    num_sum[3] = alpha_dict['R']
    alpha_dict['H'] -= num_sum[3]
    alpha_dict['E'] -= num_sum[3]*2
    alpha_dict['T'] -= num_sum[3]

    # 7
    num_sum[7] = alpha_dict['S']
    alpha_dict['V'] -= num_sum[7]
    alpha_dict['E'] -= num_sum[7]*2
    alpha_dict['N'] -= num_sum[7]

    # 9
    num_sum[9] = alpha_dict['E']

    ans = ''

    index = 0

    for num in num_sum:
        ans += str(index) * num
        index += 1

    print "Case #{}: {}".format(i, ans)

    # check out .format's specification for more formatting options
