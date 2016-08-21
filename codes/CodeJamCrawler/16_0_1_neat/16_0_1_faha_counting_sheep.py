"""
Google qualification round, Counting Sheep

@author: Faegheh Hasibi
"""


def counting_sheep(n):
    """Solves sheep counting problem"""
    if n == 0:
        return "INSOMNIA"

    count = 1
    digits = get_digits(n)
    while len(digits) != 10:
        count += 1
        digits.update(get_digits(n * count))
    return n * count


def get_digits(n):
    """Gets all the digits of a number"""
    digits = set()
    for char in str(n):
        digits.add(char)
    return digits


def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input().strip())
        print("Case #{}: {}".format(i, counting_sheep(n)))

if __name__ == "__main__":
    main()