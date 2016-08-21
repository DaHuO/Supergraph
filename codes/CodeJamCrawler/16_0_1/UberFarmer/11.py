from sys import stdin

def main():
    num_cases = int(stdin.readline())
    for case in range(1, num_cases + 1):
        N = int(stdin.readline())
        if N == 0:
            print "Case #{}: INSOMNIA".format(case)
            continue
        multiplier = 1
        digits_seen = set()
        while True:
            number = N * multiplier
            digits_seen |= digits_in_number(number)
            if len(digits_seen) == 10:
                print "Case #{}: {}".format(case, number)
                break
            multiplier += 1

def digits_in_number(number):
    str_num = str(number)
    digits = set()
    for digit in str_num:
        digits.add(int(digit))
    return digits

if __name__ == "__main__":
    main()
