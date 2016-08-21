def number(numbers):
    numbers.sort()
    str1 = ''.join(numbers)
    return str1


def digits(string):
    list_of_digits = []
    list_of_letters = []

    for letter in string:
        list_of_letters.append(letter)

    while "Z" in list_of_letters:                            # 0
        list_of_digits.append('0')
        for letter_to_remove in "ZERO":
            list_of_letters.remove(letter_to_remove)
    while "W" in list_of_letters:                            # 2
        list_of_digits.append('2')
        for letter_to_remove in "TWO":
            list_of_letters.remove(letter_to_remove)
    while "X" in list_of_letters:                            # 6
        list_of_digits.append('6')
        for letter_to_remove in "SIX":
            list_of_letters.remove(letter_to_remove)
    while "U" in list_of_letters:                            # 4
        list_of_digits.append('4')
        for letter_to_remove in "FOUR":
            list_of_letters.remove(letter_to_remove)
    while "R" in list_of_letters:                            # 3
        list_of_digits.append('3')
        for letter_to_remove in "THREE":
            list_of_letters.remove(letter_to_remove)
    while "F" in list_of_letters:                            # 5
        list_of_digits.append('5')
        for letter_to_remove in "FIVE":
            list_of_letters.remove(letter_to_remove)
    while "O" in list_of_letters:                            # 1
        list_of_digits.append('1')
        for letter_to_remove in "ONE":
            list_of_letters.remove(letter_to_remove)
    while "V" in list_of_letters:                            # 7
        list_of_digits.append('7')
        for letter_to_remove in "SEVEN":
            list_of_letters.remove(letter_to_remove)
    while "T" in list_of_letters:                            # 8
        list_of_digits.append('8')
        for letter_to_remove in "EIGHT":
            list_of_letters.remove(letter_to_remove)
    while "N" in list_of_letters:                            # 9
        list_of_digits.append('9')
        for letter_to_remove in "NINE":
            list_of_letters.remove(letter_to_remove)

    return number(list_of_digits)


f = open('A-large.in', 'r')
testsNumber = int(f.readline())
casesList = []
while testsNumber > 0:
    casesList.append(f.readline())
    testsNumber -= 1
f.close()

output = open('large-output.txt', 'w')

for case in range(len(casesList)):
    output.write('Case #' + str(case+1) + ': ' + digits(casesList[case]) + '\n')
output.close()
