cases = int(raw_input())

#Z = zero
#G = eight
#X = six


digits = ['ZERO', 'EIGHT', 'SIX', 'TWO', 'THREE', 'SEVEN', 'FOUR', 'FIVE', 'NINE', 'ONE']
digit_dict = {'SEVEN': 7, 'NINE': 9, 'SIX': 6, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'ZERO': 0, 'EIGHT': 8, 'FIVE': 5, 'ONE': 1}

for i in range(0, cases):
    s = raw_input()
    letters = {'E': 0, 'G': 0, 'F': 0, 'I': 0, 'H': 0, 'O': 0, 'N': 0, 'S': 0, 'R': 0, 'U': 0, 'T': 0, 'W': 0, 'V': 0, 'X': 0, 'Z': 0}
    for letter in s:
        letters[letter] += 1
    number = ''
    for digit in digits:
        while True:
            if all(letters[letter] is not 0 for letter in digit):
                for letter in digit:
                    letters[letter] -= 1
                number += str(digit_dict[digit])
            else:
                break    
    print 'Case #' + str(i + 1) + ': ' +''.join(sorted(number))
