for j in range(int(input())):
    ans = False
    digits = [None] * 10
    for i in range(10):
        digits[i] = 0
    n = input()
    print('Case #' + str(j+1)+':', end=' ')
    if int(n) == 0:
        print('INSOMNIA')
        continue
    i = 1
    while(ans == False):
        num = str(i * int(n))
        for c in num:
            x = int(c)
            if digits[x] == 0:
                digits[x] = 1
        for k in range(10):
            if digits[k] == 1:
                ans = True
            else:
                ans = False
                break
        i += 1
    if ans == True:
        print(num)
    else:
        print('INSOMNIA')
