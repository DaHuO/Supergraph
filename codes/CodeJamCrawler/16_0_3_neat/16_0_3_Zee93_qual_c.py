'''
CodeJam qualification round:
    Problem C. Coin Jam
'''


# TODO: More efficient way for finding if a number is prime.
def check_number_not_prime(num):
    ''' checks if a number is not prime and returns a divisor'''
    _max = num if num <= 100000 else 100000
    for i in range(2, _max):
        # print('Searching for not prime through these numbers' + str(num))
        if num % i == 0:
            return i
    return False


def get_possible_ints(binary):
    for base in range(2, 11):
        yield int(binary, base=base)


def check_number_is_jamcoin(num):
    to_return = []
    for number in get_possible_ints(num):
        res = check_number_not_prime(number)
        if not res:  # Failed
            return False
        to_return.append(res)
    return to_return


def possible_solutions(l):
    # l is the length of the binary number
    _min = '1' + '0' * (l - 2)
    _max = '1' * (l - 1)
    print('Min = ' + str(_min))
    print('Max = ' + str(_max))
    for i in range(int(_min, base=2), int(_max, base=2) + 1):
        yield bin(i)[2:] + '1'


with open('C-large.in') as f:
    f.readline()  # the first line is always one
    length, number_of_required_results = map(int, f.readline()[:-1].split(' '))

valid_solutions = []
for sol in possible_solutions(length):
    is_val = check_number_is_jamcoin(sol)
    if not is_val:  # not valid
        pass
    else:
        valid_solutions.append(sol + ' ' + ' '.join(map(str, is_val)) + '\n')
    if len(valid_solutions) == number_of_required_results:
        break


with open('c.out', mode='r+') as f:
    f.write('Case #1: \n')
    f.writelines(valid_solutions)
