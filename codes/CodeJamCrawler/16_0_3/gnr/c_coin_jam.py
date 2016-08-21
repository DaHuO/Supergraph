__author__ = 'dilip'

import math

def poss_jamcoin(poss_combo_n):
    count = pow(2, poss_combo_n)
    for num in xrange(count):
        format_str = '1{0:0' + str(poss_combo_n) + 'b}1'
        bin_str = format_str.format(num)
        yield bin_str

def bin_to_base(bin_str, base):
    sum = 0
    for i, coef in enumerate(reversed(bin_str)):
        sum = sum + int(coef) * pow(base, i)
    return sum

def checkprime(num):
    if num == 2:
        return -1
    sqrt_num = int(math.ceil(math.sqrt(num)))
    for i in xrange(2, sqrt_num + 1):
        if num % i == 0:
            return i
    return -1

if __name__ == '__main__':

    with open('C-small-attempt0.in') as in_file:
        t = int(in_file.readline())
        with open('C-small-attempt0.out', 'w') as out_file:
            out_file.write('Case #1:\n')
            s = in_file.readline().strip()
            n, j = (int(val) for val in s.split())

            poss_combo_n = n - 2; # first and last should always be 1

            #loop over all poss values of jamcoin
            count = 0
            for jamcoin_bin in poss_jamcoin(poss_combo_n):
                is_valid_jamcoin = True
                divlist = []
                #loop over all poss number with base from 2 to 10
                for base in range(2, 11):
                    basenum = int(jamcoin_bin, base)

                    #check if the basenum is not a prime
                    div_from_checkprime = checkprime(basenum)
                    if div_from_checkprime == -1: # it is prime
                        is_valid_jamcoin = False
                        break
                    else:
                        divlist.append(div_from_checkprime)

                if is_valid_jamcoin:
                    count = count + 1
                    div_str = ' '.join([str(div) for div in divlist])
                    out_file.write('{0} {1}\n'.format(jamcoin_bin, div_str))

                    if count == j:
                        break

            #count = findsteps(s)
            #out_file.write('Case #{0}: {1}\n'.format(i, count))