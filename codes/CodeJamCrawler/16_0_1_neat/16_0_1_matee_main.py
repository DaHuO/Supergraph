__author__ = 'matee'

def read_data():
    f = open('input.txt')
    number_of_testcases = int(f.readline())
    data_array = []
    for line in f:
        data_array.append([int(x) for x in line.split()])
    if len(data_array) != number_of_testcases:
        print "Something is wrong with this file."
    return number_of_testcases, data_array

def number_checker(number, number_set):
    for i in str(number):
        number_set.add(i)
    #print number_set
    if len(number_set) == 10:
        return True
    return False

def count_sheep(starting_number, count_number_of_iteration, number_set):
    if (number_checker(starting_number * count_number_of_iteration, number_set)):
        return True, str(starting_number * count_number_of_iteration)
    else:
        count_number_of_iteration += 1
        if count_number_of_iteration < 500:
            return count_sheep(starting_number, count_number_of_iteration, number_set)
        else:
            return False, "INSOMNIA"

def counting_sheep():
    count, data = read_data()
    f = open("output.txt",'w')
    #print "There is", count, "testcases."
    for i, item in enumerate(data):
        output =''
        for number in item:
            number_set = set()
            count_number_of_iteration = 1
            is_end, result = count_sheep(number, count_number_of_iteration, number_set)
        output =  "Case #%d: %s" % (i+1, result)
        print output
        f.write(output + '\n')
    f.close()


if __name__ == '__main__':
    counting_sheep()
