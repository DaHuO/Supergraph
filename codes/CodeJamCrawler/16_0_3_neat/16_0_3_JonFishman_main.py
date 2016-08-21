"""
python3 main.py < [input_file]
"""

from itertools import chain, product
from math import ceil, sqrt
import sys


def find_lowest_divisor(n):
    """
    Slow step. Try to improve
    :param n:
    :return:
    """
    return next((d for d in chain((2,), range(3, ceil(sqrt(n)) + 1, 2)) if n % d == 0), None)


def verify_coin(candidate_coin):
    BASES = range(2, 11)
    divisors_list = []
    for b in BASES:
        val = int(candidate_coin, b)
        lowest_divisor = find_lowest_divisor(val)
        if lowest_divisor:
            divisors_list.append(lowest_divisor)
        else:
            return None
    return {
        'coin': candidate_coin,
        'divisors': divisors_list
    }


def generate_coins(n):
    candidates = (
        '1'+''.join(i)+'1' for i in (product(['0','1'], repeat=n-2) if n > 2 else ('',))
    )
    verified = (verify_coin(c) for c in candidates)
    return verified


sys.stdin.readline()  # disregard first line. no need to use this count
current_line = sys.stdin.readline()
coin_length = int(current_line.split()[0])
results_limit = int(current_line.split()[1])
print("Case #1:")
jamcoins = generate_coins(coin_length)

printed = 0
for jamcoin in filter(None, jamcoins):
    print(jamcoin['coin'], ' '.join([str(i) for i in jamcoin['divisors']]))
    printed += 1
    if printed >= results_limit:
        break
