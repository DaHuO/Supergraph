#Author = Vignesh Goutham

def name_numbers():
    f = open("A-large.in","r+")
    lines = f.readlines()
    f.close()
    testcases = lines[0]
    pointer = 1

    for _n in range(int(testcases)):
        multiplier = 1
        result = []
        think_number = 0
        N = int(lines[pointer])
        check_flag = False
        if (N == 0):
            check_flag = True
            think_number = "INSOMNIA"
        else:
            while (check_flag != True):
                think_number = multiplier * N
                for number in str(think_number):
                    result.append(int(number))
                check_flag = check_if_sleep(result)
                multiplier += 1
        if (check_flag == True):
            out = "Case #{0}: {1}".format(pointer,think_number)
            print(out)
            f_out = open("result.txt","a")
            f_out.write(out)
            f_out.write("\n")
            f_out.close()

        pointer += 1


def check_if_sleep(result):
    res_set = set(result)
    for x in range(0,10):
        if x not in res_set:
            return False
    return True



if __name__ == "__main__":
    name_numbers()




