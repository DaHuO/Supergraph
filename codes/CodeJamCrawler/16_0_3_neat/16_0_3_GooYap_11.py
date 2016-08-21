import math

n = input()
a, b = map(int, input().split(' '))
print ("Case #1:")
count = 0;
cur = 0;
while (count < b):
    ar = [0 for i in range(0, 100)]
    i = a - 2
    n = cur
    while(i >= 1):
        ar[i] = n % 2
        n = n//2
        i -= 1
    ar[0] = 1
    ar[a-1] = 1
    div = [0 for i in range(0, 100)]
    kk = 0
    for base in range(2, 11):
        rez = 0
        poww = 1
        i = a - 1
        while (i >= 0):
            rez += ar[i] * poww
            poww *= base
            i -= 1
        number = rez
        for j in range(2, int(math.sqrt(number)) + 2):
            if (number % j == 0):
                div[base] = j
                kk += 1
                break                               
    if (kk >= 9):
        for i in range(0, a):
            print(ar[i], end = '')
        print(' ', end = '')
        for i in range(2, 10):
            print(div[i], end = '')
            print(' ', end = '')
        print(div[10])
        count += 1
    cur += 1
    kkk = 0
