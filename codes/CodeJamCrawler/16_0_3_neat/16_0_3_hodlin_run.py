from math import sqrt
FILENAME = 'testcase'


def to_base(number, base):
    multiplier = [base**n for n in range(len(number))]
    number = map(int, number)
    return sum([m*n for m, n in zip(reversed(multiplier), number)])


def is_prime(number):
    for devider in range(2, int(sqrt(number)) + 1):
        if (number % devider) == 0:
            return False
    return True


def get_devider(number):
    for devider in range(2, number):
        if number % devider == 0:
            return devider


def check_for_primarity(number):
    for base in range(2, 10 + 1):
        if is_prime(to_base(number, base)):
            return False
    return True


with open('{}.in'.format(FILENAME), 'r') as f:
    input = list(map(int, f.read().split()))
    string_length = input[1]
    number_of_coins = input[2]

posibilities_number = 2**(string_length-2)
max_number = to_base(''.join(['1' for _ in range(string_length-2)]), 2)

with open('{}.out'.format(FILENAME), 'w') as f:
    f.write('Case #{case}:\n'.format(case=input[0]))
    outputed = 0
    for posibility in range(posibilities_number):
        number = '{0:0{number}b}'.format(posibility, number=string_length-2)
        number = '1' + number + '1'
        if check_for_primarity(number):
            outputed += 1
            # f.write('{coin} {v2}:{b2} {v3}:{b3} {v4}:{b4} {v5}:{b5} {v6}:{b6} {v7}:{b7} {v8}:{b8} {v9}:{b9} {v10}:{b10}\n'
            f.write('{coin} {b2} {b3} {b4} {b5} {b6} {b7} {b8} {b9} {b10}\n'
                    .format(coin=number,
                            b2=get_devider(to_base(number, 2)),
                            b3=get_devider(to_base(number, 3)),
                            b4=get_devider(to_base(number, 4)),
                            b5=get_devider(to_base(number, 5)),
                            b6=get_devider(to_base(number, 6)),
                            b7=get_devider(to_base(number, 7)),
                            b8=get_devider(to_base(number, 8)),
                            b9=get_devider(to_base(number, 9)),
                            b10=get_devider(to_base(number, 10)),
                            ))
        if outputed == number_of_coins:
            break

                            # v2=to_base(number, 2),
                            # v3=to_base(number, 3),
                            # v4=to_base(number, 4),
                            # v5=to_base(number, 5),
                            # v6=to_base(number, 6),
                            # v7=to_base(number, 7),
                            # v8=to_base(number, 8),
                            # v9=to_base(number, 9),
                            # v10=to_base(number, 10)