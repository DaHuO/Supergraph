def list_maker(pancakes_str):
    pancakes_lst = []
    for i in pancakes_str:
        pancakes_lst.append(True if i == '+' else False)
    return pancakes_lst

def flip_pancakes(number, pancakes_lst):
    temp_lst = []
    temp_lst[:] = pancakes_lst[:]
    for i in range(number):
        temp_lst[number - 1 - i] = not pancakes_lst[i]
    return temp_lst

def check_happy_list(pancakes_lst):
    for p in pancakes_lst:
        if not p:
            return False
    return True

def strike_on_list(pancakes_lst):
    true_side = pancakes_lst[0]
    for i in range(len(pancakes_lst) - 1):
        if pancakes_lst[i + 1] != true_side:
            return i + 1
    return len(pancakes_lst)


if __name__ == "__main__":
    input_file_path = r"c:\tal\revenge_of_the_pancakes\B-large.in"
    output_file_path = r"c:\tal\revenge_of_the_pancakes\B-large.ou"
    with open(input_file_path, "rb") as input_file, open(output_file_path, "wb") as output_file:
        cases = int(input_file.readline())
        for i in range(cases):
            pancakes_str = input_file.readline().strip()
            main_pancakes_lst = list_maker(pancakes_str)
            flipp_times = 0
            while not check_happy_list(main_pancakes_lst):
                main_pancakes_lst = flip_pancakes(strike_on_list(main_pancakes_lst), main_pancakes_lst)
                flipp_times += 1
            output_file.write("Case #{0}: {1}\r\n".format(i + 1, flipp_times))