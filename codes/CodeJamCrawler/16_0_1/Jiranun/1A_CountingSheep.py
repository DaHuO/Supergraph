__author__ = 'Jiranun.J'

n_test_case = int(raw_input())  # read a line with a single integer

for i in range(n_test_case):
    N = int(raw_input())
    if N == 0:
        print 'Case #'+str(i+1)+': INSOMNIA'
        continue
    check = [0,0,0,0,0,0,0,0,0,0]
    mult = 1
    number = N
    while not all(check):
        number = N*mult
        mult += 1
        str_num = str(number)
        for c in str_num:
            check[int(c)] = 1
    print 'Case #'+str(i+1)+': '+str(number)

