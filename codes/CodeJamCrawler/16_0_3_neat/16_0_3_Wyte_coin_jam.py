from math import sqrt, ceil

input()
print('Case #1:')
n, j = (int(x) for x in input().split(' '))
count = 0
for i in range(0, 2**(n-2)):
    num = '1'
    for x in range(n-2):
        num += str(i%2)
        i //= 2
    num += '1'
    num = num[::-1]
    divisor = []
    for base in range(2, 11):
        val = 0
        for digit in num:
            val *= base
            val += int(digit)
        if val%2 == 0:
            divisor.append(2)
            continue
        prime = True
        for x in range(3, ceil(sqrt(val)), 2):
            if val%x == 0:
                divisor.append(x)
                prime = False
                break
        if prime:
            break
    if len(divisor) == 9:
        print(num, end='')
        for x in divisor:
            print(' {}'.format(x), end='')
        print()
        count += 1
        if count == j:
            break
