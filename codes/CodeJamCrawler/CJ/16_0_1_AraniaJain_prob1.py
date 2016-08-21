test_cases = []

num_cases = int(input("Enter number of test cases: "))
i=0
while(i<num_cases):
    test_cases.append(int(input()))
    i+=1

i=0
while(i<len(test_cases)):
    num = test_cases[i]
    digit_list = []
    count = 0
    if not num is 0:
        while(len(digit_list) < 10):
          count+=1
          test_num = num*count
          testc_num = test_num
          while(testc_num>0):
            test_digit = testc_num % 10
            testc_num = testc_num / 10

            if not test_digit in digit_list:
              digit_list.append(test_digit)

        result = count*num

    else:
        result = "INSOMNIA"
    print "Case #{}: {}".format(i+1, result)
    i+=1
