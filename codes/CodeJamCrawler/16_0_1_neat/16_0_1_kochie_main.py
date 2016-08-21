__author__ = 'Robert'


def main():
    with open("A-large.in") as input_data:
        data = input_data.readlines()

    for i in range(1, len(data)):
        solution = count_sheep(data[i][0:-1])
        print("Case #{0}: {1}".format(i, solution))
        with open("A-large.out", "a") as out_data:
            out_data.write("Case #{0}: {1}\n".format(i, solution))


def count_sheep(number):
    number = int(number)
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    a = number
    if number == 0:
        return "INSOMNIA"
    else:
        while numbers:
            a = str(a)
            for digit in a:
                if digit in numbers:
                    numbers.remove(digit)
                else:
                    pass

            a = int(a)
            a += number
        return a - number

if __name__ == '__main__':
    main()
