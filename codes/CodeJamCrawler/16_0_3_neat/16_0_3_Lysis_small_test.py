from coin_gen import generate_coins
from test_prim import test_not_prime
from shiftbase import int_in_base
N = 16
J = 50
# n is a list
print("Case #1:")
cases_num = 0
#generate_coins(N)
for coin in generate_coins(N):
    divisors = []
    coin_i = int(coin)
    valid = True
    for i in range(2,11):
        div = test_not_prime(int_in_base(coin_i, i))
        if div > 0:
            divisors.append(div)
        else:
            valid = False
            break
    if valid:
        cases_num += 1
        print(coin, end=" ")
        for i, div in enumerate(divisors):
            print(div, end="")
            if i != 8:
                print(" ", end="")
        if cases_num == 50:
            break
        else:
            print()
