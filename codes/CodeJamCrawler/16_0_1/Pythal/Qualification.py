##Counting Sheep

def check_list(lst):
    for i in lst:
        if i == False:
            return False
    return True

def reset_list():
    lst = []
    for i in range(10):
        lst.append(False)
    return lst

def next_number(number, lst, times):
    number *= times
    ##print number
    for j in str(number):
        lst[int(j)] = True
    ##print lst
    times += 1
    return lst, times


if __name__ == "__main__":
    input_file_path = r"C:\tal\counting_sheep\A-large.in"
    output_file_path = r"c:\tal\counting_sheep\output-large.ou"
    range_lst = []
    with open(input_file_path, "rb") as input_file, open(output_file_path, "wb") as output_file:
        cases = int(input_file.readline())
        for i in range(cases):
            range_lst = reset_list()
            number = int(input_file.readline())
            ##print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ {0} $$$".format(number)
            if number == 0:
                output_file.write("Case #{0}: INSOMNIA\r\n".format(i + 1))
                continue
            times_mul = 1
            (range_lst, times_mul) = next_number(number, range_lst, times_mul)
            while (not check_list(range_lst)):
                (range_lst, times_mul) = next_number(number, range_lst, times_mul)
            output_file.write("Case #{0}: {1}\r\n".format(i + 1, number * (times_mul - 1)))