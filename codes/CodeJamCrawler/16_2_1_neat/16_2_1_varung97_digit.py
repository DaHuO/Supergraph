import sys

def extract_digit(lets, letters):
    for let in letters:
        lets[let] -= 1

def digit(line):
    lets = {}
    for let in line:
        if let in lets:
            lets[let] += 1
        else:
            lets[let] = 1
    nums = ''
    if 'Z' in lets:
        while lets['Z'] >= 1:
            extract_digit(lets, 'ZERO')
            nums += '0'
    if 'W' in lets:
        while lets['W'] >= 1:
            extract_digit(lets, 'TWO')
            nums += '2'
    if 'X' in lets:
        while lets['X'] >= 1:
            extract_digit(lets, 'SIX')
            nums += '6'
    if 'G' in lets:
        while lets['G'] >= 1:
            extract_digit(lets, 'EIGHT')
            nums += '8'
    if 'S' in lets:
        while lets['S'] >= 1:
            extract_digit(lets, 'SEVEN')
            nums += '7'
    if 'H' in lets:
        while lets['H'] >= 1:
            extract_digit(lets, 'THREE')
            nums += '3'
    if 'R' in lets:
        while lets['R'] >= 1:
            extract_digit(lets, 'FOUR')
            nums += '4'
    if 'F' in lets:
        while lets['F'] >= 1:
            extract_digit(lets, 'FIVE')
            nums += '5'
    if 'O' in lets:
        while lets['O'] >= 1:
            extract_digit(lets, 'ONE')
            nums += '1'
    if 'N' in lets:
        while lets['N'] >= 1:
            extract_digit(lets, 'NINE')
            nums += '9'
    return ''.join(sorted(nums))

if __name__ == '__main__':
    test = open(sys.argv[1], 'r')
    for i in range(int(test.readline().strip())):
        line = test.readline().strip()
        print('Case #' + str(i + 1) + ': ' + str(digit(line)))
