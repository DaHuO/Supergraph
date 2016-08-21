import sys

input = sys.stdin.readlines()

def count_letters(str):
    rez = [0] * 26
    for letter in str:
        rez[index(letter)] += 1
    return rez

def subtract(counts1, counts2, multiplier):
    for i in range(len(counts1)):
        counts1[i] -= counts2[i] * multiplier
        
def index(letter):
    return ord(letter) - ord('A')

numbers = [
    count_letters("ZERO"),
    count_letters("ONE"),
    count_letters("TWO"),
    count_letters("THREE"),
    count_letters("FOUR"),
    count_letters("FIVE"),
    count_letters("SIX"),
    count_letters("SEVEN"),
    count_letters("EIGHT"),
    count_letters("NINE")
]

ordering = [
    (0, 'Z'),
    (2, 'W'),
    (4, 'U'),
    (6, 'X'),
    (8, 'G'),
    (1, 'O'),
    (3, 'H'),
    (7, 'S'),
    (5, 'V'),
    (9, 'I')
]

for t, line in enumerate(input[1:]):
    letters = count_letters(line.strip())
    digits = [0] * 10
    for number, letter in ordering:
        digits[number] = letters[index(letter)]
        subtract(letters, numbers[number],  digits[number])
    print("Case #{}: ".format(t + 1), end='')
    for digit in range(len(digits)):
        print(str(digit) * digits[digit], end='')
    print()
    
