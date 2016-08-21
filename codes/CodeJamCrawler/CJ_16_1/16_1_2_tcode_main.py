input_f = open("input.in", "r")
output_f = open("output.txt", "w")

testcase = int(input_f.readline())
for i in range(testcase):
    num_n = int(input_f.readline().replace("\n",""))
    str_input_gird=[]
    input_gird=[]
    for j in range(2*num_n-1):
        str_input_gird.append(input_f.readline().replace("\n",""))
    for each in str_input_gird:
        input_gird.append(each.split(" "))

    numbers = {}

    for each in input_gird:
        for each_num in each:
            if not each_num in numbers.keys():
                numbers[each_num] = 1
            else:
                numbers[each_num] += 1

    answer =[]
    for each_number in numbers:
        if(numbers[each_number]%2 == 1):
            answer.append(int(each_number))

    str_answer =""
    answer.sort()


    output_f.write("Case #%d: " % (i+1))

    for each_num in range(len(answer)-1):
        output_f.write(str(answer[each_num])+ " ")
    output_f.write(str(answer[len(answer)-1])+ "\n")

input_f.close()
output_f.close()