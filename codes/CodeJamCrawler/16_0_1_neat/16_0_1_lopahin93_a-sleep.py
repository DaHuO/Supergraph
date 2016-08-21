def get_answer(n):
    if n == 0:
        return "INSOMNIA"
    digits = list(range(10))
    new_n = n
    start_n = n
    while len(digits) > 0:
        n = new_n
        new_n += start_n
        digits_current_n = get_digits_of_number(n)
        for d in digits_current_n:
            if d in digits:
                index_d = digits.index(d)
                del digits[index_d]
    return str(n)


def get_digits_of_number(number):
    digits = []
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number = number // 10
    return digits


count_test = int(input())
for i in range(1, count_test + 1):
    n = int(input())
    answer = get_answer(n)
    print ("Case #{0}: {1}".format(i, answer))