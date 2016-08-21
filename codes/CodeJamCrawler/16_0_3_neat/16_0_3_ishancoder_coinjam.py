import random


def convert_to_decimal(number, base):
    final_number = 0
    position = 0
    while number > 0:
        current = number % 10
        final_number += current*(base**position)
        number //= 10
        position += 1
    return final_number


def is_prime(number):
    upper_bound = int(number**0.5) + 1
    for x in range(2, upper_bound):
        if number % x == 0:
            return False
    return True


def random_string(N,J):
    s = ""
    for _ in range(N-2):
        s += random.choice(['0', '1'])
    return s


def create_jam_coin(N, J):
    coin_str = "1"
    valid_jam_coin = []
    while J > 0:
        middle = random_string(N, J)
        coin_str += middle + "1"
        number = int(coin_str)
        if check_jam_coin(number) and (number not in valid_jam_coin):
            valid_jam_coin.append(number)
            J -= 1
        coin_str = "1"
    return valid_jam_coin


def not_trivial_divisior(number):
    for i in range(2, number):
        if number % i == 0:
            return i
    return None


def print_all_divisior(number):
    for i in range(2, 11):
        num = convert_to_decimal(number, i)
        print(not_trivial_divisior(num), end=" ")
    print()


def check_jam_coin(number):
    for base in range(2, 11):
        if is_prime(convert_to_decimal(number, base)):
            return False
    return True

if __name__ == '__main__':
    x=input()
    A = input().split()
    N = int(A[0])
    J = int(A[1])
    coins = create_jam_coin(N, J)
    print("Case #1:")
    for x in coins:
        print(x, end=" ")
        print_all_divisior(x)

