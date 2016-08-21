import sys

input = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')
cases = int(input.readline())

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(cases):
    digits_set = set(digits)
    number = int(input.readline())
    if number == 0:
        output.write("Case #" + str(i+1) + ": INSOMNIA\n")
    else:
        result = 0

        while len(digits_set) > 0:
            result += number
            result_string = str(result)
            for j in range(len(result_string)):
                if int(result_string[j]) in digits_set:
                    digits_set.remove(int(result_string[j]))
        output.write("Case #" + str(i+1) + ": " + str(result) + "\n")

output.close()
input.close()





