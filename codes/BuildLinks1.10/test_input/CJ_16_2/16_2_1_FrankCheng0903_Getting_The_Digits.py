file_strings = []
with open("Getting_The_Digits.txt") as data_file:
    for line in data_file:
        file_strings.append(line.strip())
test_case_number = int(file_strings[0])
file_strings.pop(0)

case = 1
for i in range(test_case_number):
    number_array = []
    scrambled_string = file_strings.pop(0)
    while len(scrambled_string) != 0:
        if "Z" in scrambled_string:
            a = scrambled_string.index("Z")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("E")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("R")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("O")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            number_array.append(0)
        elif "W" in scrambled_string:
            a = scrambled_string.index("W")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("T")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("O")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            number_array.append(2)
        elif "U" in scrambled_string:
            a = scrambled_string.index("U")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("F")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("O")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("R")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            number_array.append(4)
        elif "F" in scrambled_string:
            a = scrambled_string.index("F")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("I")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("V")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("E")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            number_array.append(5)
        elif "X" in scrambled_string:
            a = scrambled_string.index("S")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("I")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("X")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            number_array.append(6)
        elif "V" in scrambled_string:
            a = scrambled_string.index("S")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("E")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("V")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("E")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("N")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            number_array.append(7)

        elif "G" in scrambled_string:
            a = scrambled_string.index("E")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("I")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("G")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("H")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("T")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            number_array.append(8)
        elif "I" in scrambled_string:
            a = scrambled_string.index("N")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("I")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("N")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("E")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            number_array.append(9)
        elif "T" in scrambled_string:
            a = scrambled_string.index("T")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("H")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("R")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("E")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("E")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            number_array.append(3)
        elif "O" in scrambled_string:
            a = scrambled_string.index("O")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("N")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            a = scrambled_string.index("E")
            if a == len(scrambled_string) - 1:
                scrambled_string = scrambled_string[:a]
            else:
                scrambled_string = scrambled_string[:a] + scrambled_string[a+1:]
            number_array.append(1)
    number_array.sort()
    number_array = [str(x) for x in number_array]
    phone_string = "".join(number_array)
    print("Case #{}: {}".format(case, phone_string))
    case += 1
