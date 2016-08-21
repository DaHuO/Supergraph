import math
import random


def convert(value):
    d = {2: int(value,2),
         3: int(value,3),
         4: int(value,4),
         5: int(value,5),
         6: int(value,6),
         7: int(value,7),
         8: int(value,8),
         9: int(value,9),
         10: int(value)}
    return d

def check_divisibility(value):
    if value % 2 == 0:
        return 2
    for i in range(3, int(math.sqrt(value)) + 1, 2):
        if value % i == 0:
            return i
    return -1



def solve(length,number):
    to_return = {}
    upper_value = int("1"*(length - 2),2)
    curr_mid = 0
    while len(to_return.keys()) < number:
        #r = random.randint(0,upper_value)
        r_s = str(bin(curr_mid))[2:]
        current_value = "1" + ("0" * (length - 2 - len(r_s))) + r_s + "1"
        current_values = convert(current_value)
        current_base_devisor = {}
        for k in current_values.keys():
            div_value = check_divisibility(current_values[k])
            if div_value > 1:
                current_base_devisor[k]=div_value
            else:
                break

        if len(current_base_devisor.keys()) == 9:
            print current_value
            to_return[current_value] = []
            for i in range(2,11):
                to_return[current_value].append(str(current_base_devisor[i]))
            if len(to_return.keys()) == number:
                break
        curr_mid += 1

    return string_results(to_return)

def string_results(d):
    to_return = []
    for k in d.keys():
        to_return.append(k + " " + " ".join(d[k]))

    return "\n".join(to_return)



def main():
    input_file = open('C-small-attempt1.in', 'r')
    output_file = open('C-small.out', 'w')
    number_of_cases = int(input_file.readline().strip())
    for i in range(1,number_of_cases+1):
        length,number = input_file.readline().strip().split(" ")
        result = solve(int(length),int(number))
        output_file.write("Case #"+str(i)+": \n" + result + "\n")

    input_file.close()
    output_file.close()



if __name__ == "__main__":
    main()