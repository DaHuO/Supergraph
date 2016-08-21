number_of_cases = int(input())

for i in range(number_of_cases):
    print('Case #{}: '.format(i+1), end='')
    n = int(input())
    if n == 0:
        print('INSOMNIA')
    else:
        pull = set('1234567890')
        cnt = 0
        while len(pull) > 0:
            cnt += n
            pull -= set(str(cnt))
        print(cnt)
