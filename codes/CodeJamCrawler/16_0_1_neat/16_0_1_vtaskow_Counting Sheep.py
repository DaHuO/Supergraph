def break_digits(number_to_break):
    if number_to_break == 0:
        return [0]
    digits = []
    while number_to_break > 0:
        digits.append(number_to_break % 10)
        number_to_break /= 10
    digits = list(set(digits))
    return digits


def counting_sheep(number):
    numbers_so_far = [number]
    digits_so_far = []
    i = 2
    new_number = number
    while True:
        list_digits = break_digits(new_number)
        for digit in list_digits:
            if digit not in digits_so_far:
                digits_so_far.append(digit)
        numbers_so_far.append(new_number)
        if len(digits_so_far) == 1 and digits_so_far[0] == 0:
            return 'INSOMNIA'
        if len(digits_so_far) == 10:
            break
        new_number = i * number
        i += 1
    return numbers_so_far[-1]


output_file = open('largeoutput.txt', 'w')
file_ = open('A-large.in', 'r')
first_line = file_.readline()
for i in range(int(first_line)):
    result = counting_sheep(int(file_.readline()))
    output_file.write('Case #' + str(i + 1) + ': ' + str(result) + '\n')
file_.close()
output_file.close()
