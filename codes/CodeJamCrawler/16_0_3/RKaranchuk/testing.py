import sys
import random


def is_probable_prime(n, k = 7):
   # """use Rabin-Miller algorithm to return True (n is probably prime)
   # or False (n is definitely composite)"""
    if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
        return [False, False, True, True, False, True][n]
    elif n & 1 == 0:  # should be faster than n % 2
        return False
    else:
        s, d = 0, n - 1
        while d & 1 == 0:
            s, d = s + 1, d >> 1
        # Use random.randint(2, n-2) for very large numbers
        for a in random.sample(range(2, min(n - 2, sys.maxsize)), min(n - 4, k)):
            x = pow(a, d, n)
            if x != 1 and x + 1 != n:
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False  # composite for sure
                    elif x == n - 1:
                        a = 0  # so we know loop didn't continue to end
                        break  # could be strong liar, try another a
                if a:
                    return False  # composite if we reached end of this loop
        return True  # probably prime if reached end of outer loop


t = 1
n = 16
j = 50
line = str()
perm_list = [0]*51
temp_list = list()
ok = 1
nans = 0
for i in range(t):
    for mask in range(1 << n):
        if nans >= j:
            break
        line = ""
        temp_list.clear()
        for bit in range(n):
            if mask & (1 << bit):
                line += "1"
            else:
                line += "0"
        if line[0] == '0' or line[n-1] == '0':
            continue
        # print(line)
        for base in range(2, 11):
            res = 0
            for pos in range(len(line)):
                res += pow(base, pos) * int(line[len(line)-pos-1])
            if not is_probable_prime(res) and res is not 1:
                # print(res)
                for div in range(2, res):
                    if res % div == 0:
                        temp_list.append(res//div)
                        break
            else:
                ok = 0
                break
            if base == 10:
                temp_list.append(res)
        if ok:
            perm_list[nans] = temp_list[::]
            nans += 1
        else:
            ok = 1
            continue
print("Case #{0}:".format(i + 1))
for i in range(nans):
    print(perm_list[i][9], (" ".join([str(perm_list[i][num]) for num in range(9)])))
