def dec2bin(intput_str, size):

    temp = str(bin(int(intput_str)))
    temp = temp[2:]

    output = ""

    for i in range(size - len(temp)):
        output += "0"
    output += temp

    return output


def prime_checker(n):
    if n <= 1:
        return 0

    elif n <= 3:
        return 1

    elif n % 2 == 0 or n % 3 == 0:
        return 0

    i = 5
    while i**5 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 0
        i += 6

    return 1


def jam_coin_generator(input_string):

    all_bases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(2, 11):
        all_bases[x] = int(input_string, x)

    prime_flag = 0

    for x in range(2, len(all_bases)):
        if prime_checker(all_bases[x]) == 1:
            prime_flag = 1
            break

    if prime_flag == 1:
        return "Prime"

    else:
        for x in range(2, len(all_bases)):
            for i in range(2, all_bases[x]):
                temp = all_bases[x]
                if temp % i == 0:
                    all_bases[x] = i
                    break

        outputsting = ""
        outputsting += input_string
        for x in range(2, len(all_bases)):
            outputsting += " "
            outputsting += str(all_bases[x])

        return outputsting


def main():

    number_of_cases = int(input())
    lenght_of_jam_coin = int(input())
    number_of_jam_coins = int(input())

    Answer_strings = []

    solution_count = 0
    for x in range(pow(2, lenght_of_jam_coin - 2)):

        if solution_count == number_of_jam_coins:
            break

        string_to_test = "1"
        string_to_test += dec2bin(x, lenght_of_jam_coin - 2)
        string_to_test += "1"

        tempans = jam_coin_generator(string_to_test)

        if tempans is not "Prime":
            Answer_strings.append(tempans)
            solution_count += 1

    print("Case #%d:" % number_of_cases)
    for each in Answer_strings:
        print(each)


if __name__ == "__main__": main()