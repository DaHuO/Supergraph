import math
import itertools

def first_last_digit(num):
    return True if num[0] == '1' and num[-1] == '1' else False

def numberToBase(n, b):
    return int(str(n), b)

def all_bases(n):
    #this has to check for primality of the numbers
    all_nums = [numberToBase(n, x) for x in range(2, 11)]

    divisors = []
    for num in all_nums:
        check, div = is_prime(num)
        if check:
            return None
        else:
            divisors.append(div)

    return divisors

def is_prime(n):
    if n == 2:
        return True, None
    if n % 2 == 0 or n <= 1:
        return False, 2

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False, divisor
    return True, None

def run_code():
    t = int(input()) #there is only one test case here
    res = []
    n, j = map(int, input().split())
    lst = ["".join(str(x) for x in i) for i in itertools.product([0, 1], repeat=n) if i[0] == 1]
    count = 0
    for num in lst:
        num = int(num)
        if num >= 2 and first_last_digit(str(num)):
            divisors = all_bases(num)
            if divisors:
                res.append(["1", num, divisors])
                count += 1

        if count == j:
            break

    first_line = True
    for op in res:
        if first_line:
            print("Case #" + str(op[0]) + ":")
            first_line = False

        print(str(op[1]), end=" ")
        print(" ".join([str(x) for x in op[2]]))

if __name__ == "__main__":
    run_code()
