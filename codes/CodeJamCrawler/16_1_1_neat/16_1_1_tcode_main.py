input_f = open("input.in", "r")
output_f = open("output.txt", "w")

testcase = int(input_f.readline())
for i in range(testcase):
    letter_list = input_f.readline().replace("\n", "")
    answer = ""
    for num_c in range(len(letter_list)):
        if (num_c == 0):
            answer += letter_list[num_c]
        else:
            if (ord(letter_list[num_c]) >= ord(answer[0])):
                answer = letter_list[num_c] + answer
            else:
                answer = answer + letter_list[num_c]

    output_f.write("Case #%d: %s\n"%(i+1,answer))

input_f.close()
output_f.close()