import itertools
import numpy as np

number_list = []
list_count = 0
number_add = ""

input_file = open('small_set.txt', 'r')
output_file = open('small_result.txt', 'w')

case_number = input_file.readline()
case_input = input_file.readline()

case_split = case_input.split()
num_length = int(case_split[0])
jam_needed = int(case_split[1])
    

def isPrime(number):
    
    if number % 2 == 0:
        return False
    
    for x in range(3, int(number**0.5 ) + 1, 2):
        if number % x == 0:
            return False
        
    return True


def divisor(number):
    
    for integer in range(2,number):
        
        if number % integer == 0:
            
            return(integer)
        

for i in itertools.product(['0','1'], repeat=num_length):

    if i[0] == '1' and i[num_length - 1] == '1':
        number_list.append(''.join(i))
        
#print(len(number_list))
#print(number_list)
jam_count = 0
index = 0

output_file.write("Case #1:\n")


# print(result_array)

for number in number_list:
    base_count = 0
    
    for base in range(2,11):
        
        if isPrime(int(number, base)) == False:
            base_count = base_count + 1
            continue
        
        else:
            break
        
    if base_count == 9:
        outstring = "%s " % (number)
        output_file.write(outstring)
        divisor_string = ""
        
        for divisor_check in range(2,11):
            divisor_string = divisor_string + str(divisor(int(number, divisor_check))) + " "
            
        output_file.write(divisor_string)
        output_file.write("\n")
        jam_count = jam_count + 1
        print(jam_count)
        
    if jam_count == jam_needed:
        break
    
output_file.close()
input_file.close()
    

    
# for base in range(2,10):
#     print(base)
#     
#     for number in number_list:
#         converted_number = int(number, base)
#         #print(converted_number)
#         
#         for divisor in range(3,converted_number):
#             #print(divisor)
#             
#             if isPrime(converted_number) == True:
#                 numberBase_array[base][list_count] = divisor
#                 list_count = list_count + 1
#                 print(converted_number)
#                 break
#                 
#         numberBase_array[base][list_count] = 0
#         list_count = list_count + 1
    