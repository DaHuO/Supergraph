def find_largest(list):
    largest = 0
    count=0
    value=0
    for i in range(len(list)):
        if list[i] > largest:
            largest = list[i]
            value = i
    for each in list:
        if each == largest:
            count += 1
    return [value,count]

input_f = open("input.in", "r")
output_f = open("output.txt", "w")

testcase = int(input_f.readline())
for i in range(testcase):
    output_f.write("Case #%d:"%(i+1))

    num_of_parties =  int(input_f.readline().replace("\n",""))
    str_num_of_each = input_f.readline().replace("\n","").split(" ")
    num_of_each = []
    for each in str_num_of_each:
        num_of_each.append(int(each))

    while True:
        check0 = 0
        for each in num_of_each:
            if each == 0:
                check0 += 1
        if (check0 == len(num_of_each)):
            break

        if find_largest(num_of_each)[1] > 2:
            output_f.write(" "+chr(65+find_largest(num_of_each)[0]))
            num_of_each[find_largest(num_of_each)[0]] -= 1
        else:
            output_f.write(" ")
            value = num_of_each[find_largest(num_of_each)[0]]
            for i in range(len(num_of_each)):
                if num_of_each[i] == value:
                    output_f.write(chr(65+i))
                    num_of_each[i] -= 1





    output_f.write("\n")


input_f.close()
output_f.close()