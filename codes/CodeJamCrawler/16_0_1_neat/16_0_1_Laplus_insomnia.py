def insomnia(n):
    if n == 0:
        return "INSOMNIA"

    digits = []
    insomnia = False
    multiplier = 1
    while len(digits) < 10 and not insomnia:
        print(digits)
        temp_string = str(multiplier*n)
        for digit_char in range(0, len(temp_string)):
            if int(temp_string[digit_char]) in digits:
                pass
            else:
                digits.append(int(temp_string[digit_char]))
        multiplier += 1

    return (multiplier - 1) * n

file_in = open('A-large.in')
file_out = open('out-big.txt', 'w')

file_in.readline()

count = 1
for line in file_in:
    file_out.write("Case #" + str(count) + ": " + str(insomnia(int(line))) + "\n")
    count += 1

file_in.close()
file_out.close()



