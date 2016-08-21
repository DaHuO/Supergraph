import time


def check_digits(number):
    if number == 0:
        return 'INSOMNIA'
    all_nums = ''
    it = 1
    multiplied_num = 0
    while True:
        multiplied_num = number * it
        all_nums += (str(multiplied_num))
        it += 1
        if ('0' in all_nums and
                    '1' in all_nums and
                    '2' in all_nums and
                    '3' in all_nums and
                    '4' in all_nums and
                    '5' in all_nums and
                    '6' in all_nums and
                    '7' in all_nums and
                    '8' in all_nums and
                    '9' in all_nums):
            break
    return multiplied_num


start_time = time.time()

inputFile = open("A-large.in", 'r')
outputFile = open("output_file_digits.txt", 'w')

number_of_lines = int(inputFile.readline())
print(number_of_lines)

for caseNumber in range(number_of_lines):
    num = int(inputFile.readline())
    outputFile.write('Case #%d: %s\n' % (caseNumber + 1, check_digits(num)))

inputFile.close()
outputFile.close()

print("--- %s seconds ---" % (time.time() - start_time))
