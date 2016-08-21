from itertools import product
from math import sqrt

n = 32
j = 500

def generate_jcoins(n):
    return ("1" + "".join(m) + "1" for m in product("10",repeat=n-2))
def prime_test(c):
    for i in range(2,11):
        result = is_prime2(int(c,i))
        if result == True:
            return False
    return True
def divisors(c):
    out = []
    for base in range(2,11):
        n = int(c, base)
        threshold = sqrt(sqrt(sqrt(n))) /  5
        found = False
        i = 2
        while not found:
            if n % i == 0:
                found = True
            else:
                i += 1
                if i > threshold:
                    return False
        out.append(str(i))
    return out

count = 0
for c in generate_jcoins(n):
    ans = divisors(c)
    if ans:
        print(c, ' '.join(ans))
        count += 1
    # else:
    #     print("failed", c)
    if count >= j:
        break
