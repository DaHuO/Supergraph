import itertools

# Test Cases
test_cases = int(raw_input())

# Vars for input set etc
input_collection = []
all_digits = [0,1,2,3,4,5,6,7,8,9]

# Take all inputs
for x in range(1, test_cases + 1):
    input_collection.append(raw_input())

# For each input set in collection
for input_set in input_collection:
    bag_of_digits = []
    for i in itertools.count():
        number = (i+1) * int(input_set)
        splitted = map(int, str(number))
        for split_digit in splitted:
            if split_digit not in bag_of_digits:
                bag_of_digits.append(split_digit)
            bag_of_digits.sort()
        if bag_of_digits == all_digits:
            print "Case #%d: %d" %((input_collection.index(input_set) + 1), number)
            break
        if i > 200:
            print "Case #%d: INSOMNIA" %(input_collection.index(input_set) + 1)
            break
