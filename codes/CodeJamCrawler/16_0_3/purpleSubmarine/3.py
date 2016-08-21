import math

def dec_to_bin(n):
    s = ''
    x = n
    while (x != 0):
        s = str(x % 2) + s
        x //= 2
    return s

def base_b(s, b):
    ans = 0
    p = 1
    for i in xrange(len(s) - 1, -1, -1):
        if (s[i] == '1'):
            ans += p
        p *= b
    return ans

def find_divisor(num):
    i = 2
    while (i <= math.ceil(math.sqrt(num))):
        if (num % i == 0):
            return i
        i += 1
    return -1

t = int(raw_input())
print ("Case #1:")
n, j = [int(s) for s in raw_input().split(" ")]
count = 0
num_b = int(math.pow(2, n - 1) + 1)
while (count < j):
    flag = True
    b = 2
    s = dec_to_bin(num_b)
    lst = []
    while flag and (b <= 10):
        num = base_b(s, b)
        x = find_divisor(num)
        if (x != -1):
            lst.append(x)
            b += 1
        else:
            flag = False
    if flag:
        print s,
        for i in range(len(lst)):
            if (i < (len(lst) - 1)):
                print lst[i],
            else:
                print lst[i]
        count += 1
    num_b += 2