__author__ = 'Roberto'
import math

def finish(index, solution):

    print solution

    file_out.write("Case #{0}:\n{1}".format(index+1, solution))

def solve_test(index, test_case):

    print "Case: [{0}]".format(test_case)

    N, J = map(int, test_case.split(" "))
    jam_coins = compute(N, J)

    finish(index, "\n".join(jam_coins))

def is_prime_calc(num):

    if num <= 1:
        return (False, None)

    if num <= 3:
        return (True, None)

    if num % 2 == 0:
        return (False, 2)

    if num % 3 == 0:
        return (False, 3)

    i = 5
    counter = 100000
    while i*i <= num:
        if num % i == 0:
            return (False, i)

        if num % (i+2) == 0:
            return (False, i+2)
        i += 6

        counter -= 1
        if counter == 0:
            return (True, None)

    return (True, None)

def is_prime(num):

    if not primes.has_key(num):
        primes[num] = is_prime_calc(num)

    return primes[num]

def calc_num_in_base(jam_coin, base):

    num_in_base = 0
    no_bits = len(jam_coin)
    for i in xrange(no_bits):
        num_in_base += base**(no_bits-1-i) * jam_coin[i]

    return num_in_base

def compute(N, J):

    current_num = int(pow(2, N - 1) + 1)

    jam_coins = []
    counter = 0

    max_num = pow(2, N)
    while current_num <= max_num:

        jam_coin = bin(current_num)[2:]

        is_valid = True
        divisors = []
        for i in xrange(2, 11):
            num_in_base = int(jam_coin, i)
            (num_is_prime, divisor) = is_prime(num_in_base)

            if num_is_prime:
                is_valid = False
                break

            divisors.append(divisor)

        if is_valid:
            counter += 1
            jam_coins.append("{0} {1}".format(jam_coin, " ".join(map(str, divisors))))
            print jam_coin

        if counter % 10 == 0:
            print counter

        current_num += 2
        if counter >= J:
            break

    return jam_coins

task = "C"
level = 2
attempts = 0

if level == 0:
    file_name = "sample.in"
elif level == 1:
    file_name = "{0}-small-attempt{1}.in".format(task, attempts)
else:
    file_name = "{0}-large.in".format(task)



file_out_name = file_name.replace("in", "out")
file_out = open(file_out_name, 'w')

with open(file_name, 'r') as file:
    content = file.read()

lines = content.split('\n')
number_of_lines = int(lines[0])

test_cases = lines[1:]
primes = {}

for i in xrange(0, number_of_lines):

    solve_test(i, test_cases[i])

    file.close()

file_out.close()