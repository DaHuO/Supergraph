
def last_num(num, i):
    if num == 0:
        return 'Case #' + str(i) + ': INSOMNIA'
    digits = set()
    counter = 0
    while len(digits) != 10:
        counter += 1
        suma = num * counter
        digits = digits | get_digits(suma)
    return 'Case #' + str(i) + ': ' + str(suma)


def get_digits(num):
    digits = []
    while num != 0:
        digits.append(num % 10)
        num = num // 10
    return set(digits)



# MAIN
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()[1:]):
        print(last_num(int(line), i+1))

