text_file = open("output.txt", "w")

with open('input.txt') as f:
    lines = f.readlines()

test_cases = int(lines[0].strip())

max_try_count = 1000


def find_and_delete(N, numbers_to_see):
    for char in N:
        if char in numbers_to_see:
            numbers_to_see.remove(char)
    return numbers_to_see


for i in range(1, test_cases+1):
    numbers_to_see = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    count = 1
    N = lines[i]
    result = ""
    while True:
        if count > max_try_count:
            result = "INSOMNIA"
            break

        test_number = str(int(N.strip())*count)
        numbers_to_see = find_and_delete(test_number, numbers_to_see)
        #print numbers_to_see
        count = count +1

        if len(numbers_to_see) == 0:
            #print test_number
            result = "NOT_INSOMNIA"
            break

    if result == "INSOMNIA":
        #print result
        text_file.write("Case #{0}: {1}\n".format(i, result))
    else:
        #print test_number
        text_file.write("Case #{0}: {1}\n".format(i, test_number))

