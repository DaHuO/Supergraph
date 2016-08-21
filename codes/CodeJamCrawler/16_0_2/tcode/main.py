input_f = open("input.in", "r")
output_f = open("output.txt", "w")

testcase = int(input_f.readline())
for i in range(testcase):
    str = input_f.readline()
    if str[0] == "+":
        answer = 0
    else:
        answer = 1

    for each in range(1,len(str)):
        if (str[each-1] == "+"):
            if(str[each] == "+"):
                answer += 0
            elif(str[each] == "-"):
                answer += 2
        elif (str[each-1] == "-"):
            if(str[each] == "+"):
                answer += 0
            if(str[each] == "-"):
                answer += 0
    output_f.write("Case #%d: %d\n" % ((i+1),answer))




input_f.close()
output_f.close()