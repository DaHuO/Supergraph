def find_multiple_n(number):

    digits = []
    multiplier = 0

    if number == 0:
        return "INSOMNIA"

    while sorted(digits, key=int) != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        multiplier += 1
        number_temp = multiplier * number
        number_string = str(number_temp)
        for char in number_string:
            if int(char) not in digits:
                digits.append(int(char))

    return number_temp

with open("A-large.in", 'r') as input_file:
    cases = input_file.readline()
    with open("output.txt", 'w') as output_file:
        numbers = input_file.readlines()
        numbers = list(map(int, numbers))
        for n in range(len(numbers)):
            count = find_multiple_n(numbers[n])
            output_file.write("Case #{}: {}\n".format(n + 1, count))
