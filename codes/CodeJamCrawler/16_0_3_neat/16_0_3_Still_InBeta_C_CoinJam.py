"""

@author: Nishant Kumar
Date: 10-04-2016

"""

__author__ = 'Nishant Kumar'

import os

primes = []

def get_primes():
    global primes
    for num in range(2, 100000):
        is_prime = True
        for i in range(2, int(num / 2)):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)


def get_factor(number):
    global primes
    for f in primes:
        if number % f == 0:
            return f
    return None


def main():
    home_dir = r'C:\Users\Nishant\Dropbox\CodeBase\Coding Competitions\GoogleCodeJam_2016\Qualification Round'

    input_file  = os.path.join(home_dir, 'C-small-attempt0.in')
    output_file = os.path.join(home_dir, 'C-small-attempt0.out')

    f = open(input_file, 'r')
    o = open(output_file, 'w')

    total_cases = int(f.readline())
    lst = list(f)

    case_no = 1
    get_primes()

    while case_no <= total_cases:
        N = int(lst[case_no-1].split()[0])
        J = int(lst[case_no-1].split()[1])

        o.write("Case #%s:\n" % (case_no))

        max_num = 16384
        count = 0
        for num in range(0, max_num):
            skip = False
            factors = []
            bin_num = '1%s1' % (str(bin(num)[2:]).zfill(N-2))

            for base in range(2, 11):
                base_num = int(bin_num, base)

                if base_num in primes:
                    skip = True
                    break
                else:
                    factors.append(str(get_factor(base_num)))

                if skip:
                    break

            if not skip:
                if count > J:
                    break

                fac = ' '.join(factors)
                o.write('%s %s\n' % (bin_num, fac))
                count += 1

        case_no += 1

    f.close()
    o.close()

if __name__ == '__main__':
    main()