def sleep_state(number):
    """Will print INSOMNIA if conditions are not met"""
    digits = set()
    last_number = -1
    i = 2

    digits.update(get_digits(number))

    while digits != set([0,1,2,3,4,5,6,7,8,9]):
        old_number = last_number
        last_number = i * number

        digits.update(get_digits(last_number))

        i = i + 1

        if old_number == last_number:
            return "INSOMNIA"
            break

    return last_number
    
def get_digits(number):
    digits = []
    number = abs(number)
    if number == 0:
        return [0]
    while number > 0:
        digit = number % 10
        number = number / 10
        digits.append(digit)
    return digits

cases = int(input())

for case in range(0, cases):
    number = int(input())
    print("Case #{}: {}".format(case+1, sleep_state(number)))

