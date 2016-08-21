import sys 

def count_sheeps_testcase():
    testcase = count_sheeps_testcase.testcase
    testcase_str = int(testcase) + 1
    count_sheeps_testcase.counter += 1
    number = int(count_sheeps_testcase.number) * count_sheeps_testcase.counter 
    if not number:
        print "Case #%s: INSOMNIA" % testcase_str
        return	

    if not hasattr(count_sheeps_testcase, 'seen_digits'):
        count_sheeps_testcase.seen_digits = {}

    seen_digits = count_sheeps_testcase.seen_digits
    if testcase not in seen_digits:
        seen_digits[testcase] = set([])

    number_digits = list(str(number))
    seen_digits[testcase].update(number_digits)

    if len(seen_digits[testcase]) == 10:
        print "Case #%s: %s" % (testcase_str, number)
        return
    else:
        try:
            count_sheeps_testcase()
        except RuntimeError:
            return

input_file = open(sys.argv[1])
input_content = input_file.readlines()

testcase_number = int(input_content[0])
testcase_input = input_content[1:]
for testcase in range(0, testcase_number):
    input_number = testcase_input[testcase]
    count_sheeps_testcase.testcase = testcase
    count_sheeps_testcase.number = input_number
    count_sheeps_testcase.counter = 0
    count_sheeps_testcase()
