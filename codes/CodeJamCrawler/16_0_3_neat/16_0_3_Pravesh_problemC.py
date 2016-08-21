__author__ = 'pravesh'
import random
# For small set problem
N = 32
J = 500

viable_numbers = []

# use base-2 to create a list
lower = int("1" + "0" * (N-2)+'1', 2)
upper = int('1' * N, 2)

def get_divisor(n):
    for i in range(2, int(n**0.1)+1):
        if n % i == 0:
            return i
    return False

def check_if_jamcoin(N, b):
    number = int(N, b)
    return get_divisor(number)

# starting_divisors = {}
# for i in random.sample(range(lower, upper+1), 50000) :
#     #remove the 0b suffix and append
#     result = get_divisor(i)
#     if result:
#         bin_i = bin(i)[2:]
#         if not bin_i[-1] == '1': continue
#         viable_numbers.append(bin_i)
#         starting_divisors[bin_i] = result
#

print("Case #1:")
j = 0
seen = []
random.seed(31)
while True:
    # divisors = [starting_divisors[v]]
    divisors = []
    n = random.randrange(lower, upper+1)
    # if n in seen: continue
    # seen.append(n)
    v = bin(n)[2:]
    if v[-1] == '0': continue
    for b in range(2,11):
        result = check_if_jamcoin(v, b)
        if not result:
            # means that the number is prime...
            break
        else:
            # result contains the divisor in this base..
            divisors.append(result)
    else:
        # print the list of divisors
        j += 1
        print(v, *divisors)
        if j == J:
            exit(0)
