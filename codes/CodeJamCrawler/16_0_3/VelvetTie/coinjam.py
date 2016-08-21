import sys
import math

def debug_print(line):
    print(line, file=sys.stderr)

def get_range(coin_length):
    # Determine the minimum possible and maximum possible coins.
    min_coin_str = '1'
    max_coin_str = '1'
    for i in range(1, coin_length-1):
        min_coin_str += '0'
        max_coin_str += '1'
    min_coin_str += '1'
    max_coin_str += '1'
    min_value = int(min_coin_str, 2)
    max_value = int(max_coin_str, 2)
    return min_value, max_value


def find_divisor(num):
    divisor = 1

    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            divisor = n
            break

    return divisor

def is_string_prime(numstr):
    pass


def generate_coins(coin_length, num_coins):

    (min_coin, max_coin) = get_range(coin_length)
    debug_print("{} {}".format(min_coin, max_coin))
    num_coins_found = 0
    coins = {}

    for n in range(min_coin, max_coin + 1):
        # Determine a possible string of bits.
        numstr = str(bin(n))[2:]
        # Skip coins that do not end with '1'.
        if numstr[coin_length - 1] == '0':
            continue
        debug_print("Check {}".format(numstr))

        num_divisors = 0
        # TODO: Determine a divisor of the string in each base from 2 to 10, or if the number is prime.
        coins[numstr] = []
        # Check each base from 2 to 10.
        for base in range(2, 11):
            # Find a divisor for this base.
            d = find_divisor(int(numstr, base))
            # Once we've found a base where the only divisor is 1, then this coin is not valid.
            if d == 1:
                coins[numstr] = None
                break
            else:
                # Add a valid divisor to the list for this coin.
                debug_print("Found divisor {} for coin {}, base {}".format(d, numstr, base))
                coins[numstr].append(d)
                num_divisors += 1
        # Continue to the next coin.
        if coins[numstr]:
            num_coins_found += 1
        else:
            del coins[numstr]
        # End if we've found the number of coins we wanted.
        if num_coins_found == num_coins:
            break

    sorted_coins = sorted(coins.keys())
    debug_print("sorted coins: {}".format(sorted_coins))
    #print(sorted_coins)
    for c in sorted_coins:
        output = c + ' ' + ' '.join([str(num) for num in coins[c]])
        print(output)

def read_input():
    num_test_cases = int(input())
    for t in range(1, num_test_cases + 1):
        (num_length, num_coins) = (int(num) for num in input().split(' '))
        debug_print("{} {}".format(num_length, num_coins))
        print("Case #{}:".format(t))
        generate_coins(num_length, num_coins)


if __name__ == "__main__":
    read_input()