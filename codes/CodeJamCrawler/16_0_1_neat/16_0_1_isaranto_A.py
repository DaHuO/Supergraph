digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
input = []
with open('A-large.in', 'r')as fp:
    first = True
    for line in fp:
        if first:
            first = False
        else:
            input.append(int(line.rstrip()))
print input
test_case = 1
for number in input:
    if number == 0:
        with open('results.txt', 'a')as fp:
            fp.write("Case #"+ str(test_case)+": INSOMNIA")
            fp.write("\n")
            test_case += 1
    else:
        #print "start with number: ", number
        digits_dict = {0 : False, 1 : False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False}
        new_number = number
        first_time = True
        while not all(digits_dict.values()):
            if not first_time : new_number = int(new_number) + number
            first_time = False
            #print "               number is now", new_number
            for digit in digits_dict.keys():
                #print "         checking for digit :", digit
                list_of_nums = [int(x) for x in str(new_number)]
                if digit in list_of_nums:
                    #print "      removing digit :", digit, " from list"
                    digits_dict[digit] = True
            #print digits_dict
        with open('results.txt', 'a')as fp:
            fp.write("Case #"+ str(test_case)+": "+ str(new_number))
            fp.write("\n")
            test_case += 1
