import json
import sys

prime_table = []
table = {}

def construct_prime_table(max_n):
    p_cnt = 0
    for i in range(2, max_n + 1):
        is_prime = True
        for j in range(0, p_cnt):
            if i % prime_table[j] == 0:
                is_prime = False
                break
        if is_prime:
            prime_table.append(i)
            p_cnt += 1

def find_div(x):
    for i in range(0, len(prime_table)):
        if prime_table[i] ** 2 > x:
            break
        if x % prime_table[i] == 0:
            return prime_table[i]
    return -1

def is_jamcoin(x):
    arr = [0] * 11
    for base in range(2, 11):
        tmp = x
        new_val = 0
        mul = 1
        while tmp > 0:
            new_val += (tmp % 2) * mul
            mul *= base
            tmp /= 2
        div = find_div(new_val)
        if div > 0:
            arr[base] = div
        else:
            return False
    table[x] = arr
    return True

def calculate(n, j):
    table = {}
    x = 2 ** (n - 1) + 1
    while j > 0:
        if is_jamcoin(x):
            j -= 1
        x += 2

construct_prime_table(2 ** 15)

input_file = sys.argv[1]
with open(input_file, 'r') as f:
    t = int(f.readline())
    for i in range(0, t):
        print('Case #%d:' % (i + 1))
        line = f.readline().strip()
        n = int(line.split()[0])
        j = int(line.split()[1])
        calculate(n, j)
        for x, arr in table.items():
            print('%s %s' % (bin(x)[2:], ' '.join([str(ele) for ele in arr[2:]])))
