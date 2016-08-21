"""
Author: Aadil Ahamed
sheep.py: Google Code Jam Problem 1
"""


def break_digits(N):
    digits = []
    for i in range(6, -1, -1):
        div = 10 ** i
        digit = N // div
        digits.append(digit)
        N %= div
    return digits


def add_to_set(digits, bset):
    i = 0
    while digits[i] == 0:
            i += 1
    while i  < len(digits):
        bset.add(digits[i])
        i += 1
    return bset


def count_sheep(N):
    if N == 0:
        return "INSOMNIA"
    bset = set()
    for i in range(1, 10**6):
        digits = break_digits(N*i)
        add_to_set(digits, bset)
        if len(bset) == 10:
            return N*i


def test_digits():
    print(break_digits(999))


def test_count_sheep():
    print(count_sheep(5))
    print(count_sheep(0))
    print(count_sheep(1))
    print(count_sheep(2))
    print(count_sheep(11))
    print(count_sheep(1692))

def main():
    # test()    
    T = int(input())
    for i in range(T):
        N = int(input())
        print("Case #{}: {}".format(i+1, count_sheep(N)))

def test():
    test_digits()
    test_count_sheep()

if __name__ == "__main__":
    main()
