import math

N, J = 16, 50
output = "Case #1:\n"

cache = [[i ** j for j in range(1, N)] for i in range(2, 11)]

def plus_2(num_bin, lst):
    d = N - 2
    lst_bin = list(num_bin)
    while d >= 0:
        if lst_bin[d] == '1':
            lst_bin[d] = '0'
            lst = [lst[i] - cache[i][N - 2 - d] for i in range(len(lst))]
            d -= 1
        else:
            lst_bin[d] = '1'
            lst = [lst[i] + cache[i][N - 2 - d] for i in range(len(lst))]
            break
    return ''.join(lst_bin), lst

def get_divider(i):
    for k in range(2, int(math.sqrt(i)) + 1):
        if i % k == 0:
            return k
    return -1

lst = [i ** (N - 1) + 1 for i in range(2, 11)]
start = '1' + '0' * (N - 2) + '1'
while lst[0] != 1 and J > 0:
    dividers = [0] * 9
    fail = False
    for i in range(9):
        dividers[i] = get_divider(lst[i])
        if dividers[i] == -1:
            fail = True
            break
    if not fail:
        output += "{} {}\n".format(start, ' '.join(map(str, dividers)))
        J -= 1
    print start
    start, lst = plus_2(start, lst)

f_out = file('output.txt', 'w')
f_out.write(output)
f_out.close()
