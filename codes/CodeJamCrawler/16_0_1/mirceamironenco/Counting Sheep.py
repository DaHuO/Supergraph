def find_digits(number):
    new_value = number
    digits = {}
    i = 2
    while len(digits) != 10:
        a = str(new_value)
        for c in a:
            if c not in digits:
                digits[c] = True
        if len(digits) == 10:
            break
        else:
            new_value = i * number
            i += 1

    return new_value


if __name__ == "__main__":
    tests = int(input().strip())
    for i in range(tests):
        number = int(input().strip())
        if number == 0:
            print("Case #{}: INSOMNIA".format(i+1))
        else:
            value = find_digits(number)
            print("Case #{}: {}".format(i+1, value))


