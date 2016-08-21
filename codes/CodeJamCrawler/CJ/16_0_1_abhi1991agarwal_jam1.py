
def main():
    test_cases = int(raw_input())
    test_count = 1
    while test_count <= test_cases:

        num = int(raw_input())
        new_str = "Case #" + str(test_count) + ":"
        if num == 0:

            print new_str, "INSOMNIA"
        else:
            integer_dict = {}
            count = 1
            while len(integer_dict) < 10:
                new_num = num * count
                num_string = str(new_num)
                for char in num_string:
                    integer_dict[char] = 1
                count += 1

            print new_str, new_num
        test_count += 1
main()