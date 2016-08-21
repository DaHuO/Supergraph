T = int(input())

digits = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 

for i in range(T):
    k = int(input())
    if k != 0: 
        all_digits = set()

        num = k
        while True:
            for j in str(num): all_digits.add(int(j))
            if digits == all_digits:
                print('Case #' + str(i + 1) + ': ' + str(num))
                break
            else:    
                num += k
    else:
        print('Case #' + str(i + 1) + ': INSOMNIA')
