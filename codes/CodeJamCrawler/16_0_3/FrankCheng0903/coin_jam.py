import math

file_strings = []
with open("coin_jam.txt") as data_file:
    for line in data_file:
        file_strings.append(line.strip())
test_case_number = file_strings[0]
file_strings.pop(0)
two_numbers = file_strings[0].split()

length_of_coins = int(two_numbers[0])
number_of_coins = int(two_numbers[1])


def convert_into_base_n(coin, base):
    """
    Converts string coin into a natural number by interpreting in base base
    @rtype: int
    """
    coin = str(coin)
    converted_sum = 0
    for i in range(len(coin)):
        value = int(coin[-i - 1])
        converted_sum += value * (base**i)
    return converted_sum


def find_nt_factor(num):
    """
    Returns None if  num is prime. Else returns smallest non-trivial factor.
    @rtype: int | None
    """
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            return i
    return None


def is_jamcoin(binary_num):
    """
    Returns None if binary_num is not a jamcoin. Else, returns a list of
    strings - the divisors of binary_num.
    """
    num_in_string = str(binary_num)
    if num_in_string[0] == "0" or num_in_string[-1] == "0":
        return None
    divisors = []
    for i in range(2, 11):
        converted_sum = convert_into_base_n(binary_num, i)
        nt_factor_i = find_nt_factor(converted_sum)
        if nt_factor_i is None:
            return None
        else:
            divisors.append(str(nt_factor_i))
    return divisors


def find_jamcoins(size_of_coins, number_of_coins):
    """
    Finds number_of_coins jamcoins with size size_of_coins. Returns a list
    of lists, with each sublist a row in the output - a jamcoin and 9 factors.
    """
    answer_list = []
    limit = number_of_coins

    for i in range(2**(size_of_coins-1) + 1, 2**(size_of_coins), 2):

        possible_jamcoin = bin(i)[2:]
        a = is_jamcoin(possible_jamcoin)

        if a is not None:
            answer = [possible_jamcoin] + a
            answer_list.append(answer)

            if len(answer_list) == limit:
                return answer_list

a = find_jamcoins(length_of_coins, number_of_coins)
print("Case #1:")
for row in range(len(a)):
    print(" ".join(a[row]))

