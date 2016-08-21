#! venv/bin/python3.4


def all_numbers_appeared(numbers):
    """
    Function that takes an array where each nth position serves as flag if
    the (n+1)th number has appeared and return if all numbers from [0-9]
    have occured
    """
    return sum(numbers) == 10


def flag_digits(number, numbers_array):
    """
    Function that takes the array of flags and correctly sets them according
    to the digits from a number
    """
    # Seems ugly, probably costs too much RAM
    digits = list(map(int, list(str(number))))
    for digit in digits:
        numbers_array[digit - 1] = 1


cases = int(input())
results = ['INSOMNIA' for _ in range(cases)]

for case_n in range(cases):
    numbers = [0 for _ in range(10)]
    n = int(input())
    for iteration in range(1, 100000):
        m = n * iteration
        flag_digits(m, numbers)
        if (all_numbers_appeared(numbers)):
            results[case_n] = str(m)
            break
for case in range(len(results)):
    print("Case #{}: {}".format(case + 1, results[case]))
