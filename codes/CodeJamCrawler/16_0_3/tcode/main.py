from math import sqrt
def get_answer(length,level):
    if(length-2 == level):
        global num_of_answer
        if(num_of_answer > 0):
            for i in range(len(base_check)):
                base_check[i] = False


            for base in range(2,11):
                base_check[base-2] = check_prime(get_num(num,base),base)
                if (base_check[base-2] == False): break

            div_num = 0
            for each in base_check:
                if(each == True):
                    div_num+=1
            # print(div_num)
            if(div_num==9):
                output_f.write("%d "%get_num(num,10))
                for i in range(8):
                    output_f.write("%d "%base_num[i])
                output_f.write("%d\n"%base_num[8])
                num_of_answer -= 1

    else:
        for i in range(2):
            num[level+1] = i
            get_answer(length,level+1)

def check_prime(num,base):
    for i in range(2,int(sqrt(num))+1):
        if(num % i == 0):
            base_num[base-2] = i
            return True
    return False

def get_num(array,base):
    answer =0
    num = len(array)-1
    for each in array:
        answer +=(base**num)*each
        num -=1
    return answer

input_f = open("input.in", "r")
output_f = open("output.txt", "w")

input_f.readline()
output_f.write("Case #1:\n")

(str_length, str_num_of_answer) = input_f.readline().replace("\n","").split(" ")
length = int(str_length)
num_of_answer = int(str_num_of_answer)
num = []
base_check = []
base_num = []
for i in range(length):
    num.append(1)
for i in range(9):
    base_check.append(False)
    base_num.append(0)

get_answer(length,0)


input_f.close()
output_f.close()