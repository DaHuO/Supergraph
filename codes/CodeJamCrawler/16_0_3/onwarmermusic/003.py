import random
import math

def gen_candidate_jamcoin(length):
    return '1' + str(bin(random.getrandbits(length-2))[2:]) + '1'

def gen_max_divisor(length, base):
    # Get our largest divisor
    max_div_str = '';
    for i in range(1, length):
        max_div_str += '1'

    return int(max_div_str, base)

def test_jamcoin(candidate, base):
    max_divisor = int(math.sqrt(candidate))

    for i in range(2, max_divisor):
        if((candidate % i) == 0):
            return i

    return 0

def gen_jamcoins(t, line):
    print('Case #{}: {}'.format(t, flips))

def main():
    with open('C-input.in', 'r') as f:
        for line_num, line in enumerate(f):
            if(line_num == 1):
                args = line.split()
                length = int(args[0])
                coins_to_find = int(args[1])

    jamcoins = {}
        
    while(len(jamcoins) < coins_to_find):
        candid = gen_candidate_jamcoin(length)

        # Check length
        if(len(candid) < length):
            continue

        # Keep dupes out
        if(candid in jamcoins):
            continue

        valid = True
        divisors = []
        for i in range(2, 11):
            result = test_jamcoin(int(candid, i), i)
            if(result == 0):
                valid = False
                break
            else:
                divisors.append(result)

        if(valid):
            jamcoins[candid] = divisors

    print('Case #1:')
    for coin in jamcoins:
        print(coin, end=' ')
        print(' '.join(map(str, jamcoins[coin])))

if __name__ == '__main__':
    main()
