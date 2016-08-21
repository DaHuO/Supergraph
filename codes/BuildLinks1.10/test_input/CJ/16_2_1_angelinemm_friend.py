f_in = open('input.txt', 'r')
f_out = open('output.txt', 'w')

T = int(f_in.readline())

def get_phone_dict():
    return {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
    }

def remove_number(code, number):
    for letter in number:
        code.remove(letter)
    return code

for i in range(1, T+1):
    code = list(f_in.readline().rstrip('\n'))
    phone_dict = get_phone_dict()
    for char, str_number, number in [
        ('Z', 'ZERO', '0'),
        ('W', 'TWO', '2'),
        ('U', 'FOUR', '4'),
        ('X', 'SIX', '6'),
        ('G', 'EIGHT', '8'),
        ('F', 'FIVE', '5'),
        ('H', 'THREE', '3'),
        ('I', 'NINE', '9'),
        ('V', 'SEVEN', '7'),
        ('O', 'ONE', '1'),
    ]:
        while char in code:
            code = remove_number(code, str_number)
            phone_dict[number] += 1
    phone_number = ''
    for digit in sorted(phone_dict.keys()):
        number = phone_dict[digit]
        for _ in range(0, number):
            phone_number += digit
    f_out.write('Case #{}: {}'.format(i, phone_number))
    f_out.write('\n')
