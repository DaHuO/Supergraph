from itertools import combinations
from math import sqrt

def divisor(n):
    for i in range(2, min([ int(sqrt(n)), 10000])):
        if n % i == 0:
            return i
    return 1 

input()
print("Case #1:")

N, J = map(int, input().split())

ones = [10**x for x in range(1,N-1)]

for num_of_ones in range(4, N-2+1, 6):
    for num_ones in combinations(ones, num_of_ones):
        str_num = str(1 + sum(num_ones) + 10**(N-1))
        int_num = int(str_num, 2)

        if (sum(map(int, str_num[0::2])) + 2*sum(map(int, str_num[1::2]))) % 3 != 0:
            continue

        div6 = divisor(int(str_num, 6))
        if div6 == 1:
            continue

        ans = [str_num, 3, 2, 3, 2, div6, 2, 3, 2, 3]
        print(" ".join(map(str, ans)))
        
        # check_mods = [int(str_num, b) % ans[b-1] for b in range(2, 11)]
        # print(int_num, check_mods)
        
        J -= 1
        if J == 0:
            exit()
