import sys

number_of_cases = int(sys.stdin.readline().strip())

for case in range(number_of_cases):
    return_line = "Case #"+str(case+1)+": "
    N = long(sys.stdin.readline().strip())
    if N == 0:
        print(return_line+"INSOMNIA")
    else:
        M = N
        hash_table = [False]*10
        while True:
            #hash_table = [False]*10
            list_of_ints = [int(i) for i in str(M)]
            for item in list_of_ints:
                hash_table[item] = True
            if any(h==False for h in hash_table):
                M += N
            else:
                print(return_line + str(M))
                break



