__author__ = 'josephbosire'
def load_data_set():
    data_Set = {}
    NUMS_TO_BE_SEEN = ["1","2","3","4","5","6","7","8","9","0"]
    with open("answers.out", "wb") as answer_file:
        with open("A-large.in", "rb") as input_file:
            number_of_cases = input_file.readline()
            cases = [int(line.strip("\n")) for line in input_file.readlines()]
            print cases
            count = 1
            for case in cases:
                print case
                nums_remaining = set(NUMS_TO_BE_SEEN)
                last_number_to_be_named = "INSOMNIA"
                multiplier = 1
                if case * 2 != case:
                    while True:
                        case_as_list = list(str(case*multiplier))
                        nums_remaining = nums_remaining - set(case_as_list)
                        if len(nums_remaining) == 0:
                            last_number_to_be_named = case*multiplier
                            break
                        multiplier += 1
                answer_file.write("Case #{}: {}\n".format(count, last_number_to_be_named))
                count += 1

print load_data_set()


