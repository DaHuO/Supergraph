import sys

test_file = open(sys.argv[1], 'r')
test = test_file.read().split('\n')
test_file.close()

total = int(test[0])

output = ""

for i in range(total):
    if int(test[i + 1]) == 0:
        output = output + 'Case #' + str(i + 1) + ': INSOMNIA\n'
    else:
        digits = []
        complete = False
        count = 1
        query = int(test[i + 1])

        for j in range(10):
            digits.append(False)

        while complete == False:
            
            prod = query * count
            split_nums = list(str(prod))
            for j in range(len(split_nums)):
                digits[int(split_nums[j])] = True

            is_complete = True
            for j in range(len(digits)):
                if digits[j] == False:
                    is_complete = False

            if is_complete:
                output = output + 'Case #' + str(i + 1) + ': ' + str(prod) + '\n'
                complete = True
            else:
                count = count + 1


print output

output_file = open('output.txt', 'w')
output_file.write(output)
output_file.close()