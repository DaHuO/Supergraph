def jamcoin_generator(n, j):
    legit_coins = {}
    num_divisors = 9
    base = 10**(n-1) + 1
    divisors = get_divisors(base)
    if len(divisors) == num_divisors:
        j-=1
        legit_coins[base] = divisors
    if j == 0:
        return legit_coins
    decimal = convert_to_decimal(base)

    final = base
    i = 10
    while i < base - 1:
        final += i
        i *= 10

    final_decimal = convert_to_decimal(final) + 1

    for i in range(decimal+2,final_decimal, 2):
        coin = convert_to_binary(i)
        divisors = get_divisors(coin)
        if len(divisors) == num_divisors:
            j-=1
            legit_coins[coin] = divisors
        if j == 0:
            break

    return legit_coins


def get_divisors(coin):
    coin_values = get_interpretations(coin)
    divisors = []
    for value in coin_values:
        for num in range(2, int(value**0.5) + 1):
            if value % num == 0:
                divisors.append(num)
                break
    return divisors


def get_interpretations(jamcoin):
    base = 2
    interpretations = []
    while base <= 10:
        interpretation = 0
        power = len(str(jamcoin))-1
        for digit in str(jamcoin):
            interpretation += int(digit)*(base**power)
            power -= 1
        interpretations.append(interpretation)
        base += 1
    return interpretations


def convert_to_decimal(num):
    interpretation = 0
    power = len(str(num))-1
    for digit in str(num):
        interpretation += int(digit)*(2**power)
        power -= 1
    return interpretation


def convert_to_binary(num):
    s = ''
    while num != 0:
        bit = num % 2
        num = num // 2
        s+= str(bit)
    return s[-1: -len(s)-1:-1]


if __name__ == '__main__':
    inp = open("small_input.txt", "r")
    out = open("small_output.txt","w")
    test_cases = [x.strip('\n') for x in inp.readlines()]
    test_case_num = 1
    while test_case_num <= int(test_cases[0]):
        test_case = test_cases[test_case_num]
        n = test_case[0:test_case.index(' ')]
        j = test_case [test_case.index(' ')+1:]
        jamcoins = jamcoin_generator(int(n), int(j))
        out.write('Case #{}:\n'.format(test_case_num))
        for coin in jamcoins:
            str_divisors = ''
            for divisor in jamcoins[coin]:
                str_divisors += " " + str(divisor)
            out.write('{}{}\n'.format(coin, str_divisors))
        test_case_num += 1


