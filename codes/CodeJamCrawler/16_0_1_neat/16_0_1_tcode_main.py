input_f = open("input.in", "r")
output_f = open("output.txt", "w")

testcase = int(input_f.readline())
for i in range(testcase):
    num_n = int(input_f.readline())
    quit_loop = False
    num_i=1
    digits = {
        "0":False,
        "1":False,
        "2":False,
        "3":False,
        "4":False,
        "5":False,
        "6":False,
        "7":False,
        "8":False,
        "9":False,
    }
    while quit_loop == False:
        temp = num_n*num_i
        str_temp = str(temp)
        for each in str_temp:
            if(int(each)==0): digits["0"]=True
            if(int(each)==1): digits["1"]=True
            if(int(each)==2): digits["2"]=True
            if(int(each)==3): digits["3"]=True
            if(int(each)==4): digits["4"]=True
            if(int(each)==5): digits["5"]=True
            if(int(each)==6): digits["6"]=True
            if(int(each)==7): digits["7"]=True
            if(int(each)==8): digits["8"]=True
            if(int(each)==9): digits["9"]=True

        if(digits["0"] and
           digits["1"] and
           digits["2"] and
           digits["3"] and
           digits["4"] and
           digits["5"] and
           digits["6"] and
           digits["7"] and
           digits["8"] and
           digits["9"]):
            output_f.write("Case #%s: %s\n" % (str((i+1)),str_temp))
            quit_loop=True
        if num_n*num_i == num_n*(num_i+1):
            output_f.write("Case #%s: INSOMNIA\n" % str((i+1)))
            quit_loop=True

        num_i+=1





input_f.close()
output_f.close()