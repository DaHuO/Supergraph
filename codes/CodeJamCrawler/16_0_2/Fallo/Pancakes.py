__author__ = 'FalguniT'


with open("input_pancake.txt") as f:
    content = f.readlines()
no_of_test_cases = int(content[0])

for case_t in range(1,no_of_test_cases + 1):
    #small input
    n = content[case_t].strip()
    flip_required = 0
    plus_count = "+" in n

    if (n.count("+") == len(n)):
        with open("output_pancake_large.txt","a") as f_handle:
            f_handle.write('Case #'+ str(case_t) +':  ' + str(0) + '\n')

    elif (n.count("-") == len(n)):
        with open("output_pancake_large.txt","a") as f_handle:
            f_handle.write('Case #'+ str(case_t) +':  ' + str(1) + '\n')

    else:
        while n.count("-") > 0:
            idx_minus = n.rfind('-')
            print('before n', n,idx_minus, n[0:idx_minus+1])

            sub_str = n[0:idx_minus+1]
            n = sub_str.replace('+', '%temp%').replace('-', '+').replace('%temp%', '-') + n[idx_minus+1:]
            print('after n', sub_str, n, n[idx_minus:])
            flip_required =  flip_required + 1

        with open("output_pancake_large.txt","a") as f_handle:
            f_handle.write('Case #'+ str(case_t) +':  ' + str(flip_required) + '\n')