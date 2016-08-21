
from math import sqrt, floor

def get_base_number(n):
    to_return = []
    for i in range(2, 11):
        to_return.append(int(str(n), i))
    return to_return

def next_coin(jamcoin):
    jamcoin = int(bin(int(str(jamcoin), 2) + 1)[2:])
    return jamcoin

def get_divisor(n):
    if n % 2 == 0:
        return 2
    else:
        bnumber = int(floor(sqrt(n)))
        for d in range(3, bnumber + 1, 2):
            if n % d == 0:
                return d
            elif d >= bnumber:
                return -1
        return -1
if __name__ == "__main__":
    input_file = open('C-small-attempt1.in', 'r')
    N, J = [int(x) for x in input_file.read().split('\n')[1].split() if x != '']
    input_file.close()
    jamcoin = '1'
    for i in range(1, N):
        jamcoin = jamcoin+ '0'
    jamcoin = int(jamcoin)


    with open('output.txt', 'w') as f:
        f.write('Case #1:\n')
        j = 0
        while(j < J):
            if str(jamcoin)[len(str(jamcoin))-1] == '0':
                jamcoin = next_coin(jamcoin)


            bases = get_base_number(jamcoin)
            divisors = [get_divisor(n) for n in bases]
            if -1 in divisors:
                jamcoin = next_coin(jamcoin)
            else:
                # Find Divisors
                f.write(str(jamcoin))
                for d in divisors:
                    f.write(' ' + str(d))
                f.write('\n')
                j += 1
                jamcoin = next_coin(jamcoin)