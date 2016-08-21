for i in range(int(input())):
    N = int(input())
    print('Case #%d: ' % (1+i), end='')
    digits = [str(s) for s in range(10)]
    digits_bool = [False]*10
    if N == 0:
        print('INSOMNIA')
        continue

    for j in range(1,1000000):
        new_num_str = str(j*N)
        #print(new_num_str)
        #print(digits_bool)
        for k, d in enumerate(digits):
            if d in new_num_str:
                digits_bool[k] = True
        if all(d for d in digits_bool):
            print(new_num_str)
            break

