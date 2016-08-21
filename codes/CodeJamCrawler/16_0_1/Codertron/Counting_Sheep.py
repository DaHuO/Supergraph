

import os

OUTPUT_FILE_NAME = 'output_file.txt'
def Counting_Sheep():
    input_file = open('input_file.txt', 'r')
    if(os.path.isfile(OUTPUT_FILE_NAME)):
        os.remove(OUTPUT_FILE_NAME)
    first = 0
    num_tests = 0
    test_number = 0
    for line in input_file:
        if(first == 0):
            num_tests = int(line)
            first = 1
        else:
            test_number = test_number + 1
            check_number(test_number, line.strip())
            if test_number == num_tests:
                print 'Done checking!!!'
                input_file.close()
                return 0
    print 'This should not happen'
    return -1


def check_number(test_case_number, N):
    output_file = open(OUTPUT_FILE_NAME, 'a')
    test = True
    i = 1

    found_0 = False
    found_1 = False
    found_2 = False
    found_3 = False
    found_4 = False
    found_5 = False
    found_6 = False
    found_7 = False
    found_8 = False
    found_9 = False



    while(test):
        test_num = i * int(N)
        test_num_str = str(test_num)
        num_digits = len(test_num_str)

        if int(test_num_str) == 0:
            text = 'Case #'+str(test_case_number)+': INSOMNIA\n'
            output_file.write(text)
            print text
            output_file.close()
            test = False
            return 0

        for idx in range(0, num_digits):
            if not found_0 and test_num_str[idx] == '0':
                found_0 = True
            if not found_1 and test_num_str[idx] == '1':
                found_1 = True
            if not found_2 and test_num_str[idx] == '2':
                found_2 = True
            if not found_3 and test_num_str[idx] == '3':
                found_3 = True
            if not found_4 and test_num_str[idx] == '4':
                found_4 = True
            if not found_5 and test_num_str[idx] == '5':
                found_5 = True
            if not found_6 and test_num_str[idx] == '6':
                found_6 = True
            if not found_7 and test_num_str[idx] == '7':
                found_7 = True
            if not found_8 and test_num_str[idx] == '8':
                found_8 = True
            if not found_9 and test_num_str[idx] == '9':
                found_9 = True

            if found_0 and found_1 and found_2 and found_3 and found_4 and found_5 and found_6 and found_7 and found_8 and found_9:
                text = 'Case #' + str(test_case_number) + ': ' + test_num_str+'\n'
                output_file.write(text)
                print text
                print '# tries : ' + str(i) + '\n'
                output_file.close()
                test = False
                return 0
        i = i + 1

    print 'This should never happen outside while loop'



if __name__ == "__main__":
    Counting_Sheep()